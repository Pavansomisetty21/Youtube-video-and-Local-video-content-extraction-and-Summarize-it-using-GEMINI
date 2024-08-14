import streamlit as st
import os
from moviepy.editor import VideoFileClip
import speech_recognition as sr
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai

# Function to extract audio from video
def extract_audio_from_video(video_path, audio_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)
    return audio_path

# Function to convert audio to text
def audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        transcript = recognizer.recognize_google(audio_data)
    return transcript

# Function to get transcript from YouTube video
def get_transcript(yt_url):
    try:
        video_id = yt_url.split("v=")[-1].split("&")[0]
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    except Exception as e:
        return f"Error fetching transcript list for video ID {video_id}: {e}"
    
    try:
        # Find manually created transcript if available
        transcript = transcript_list.find_manually_created_transcript()
    except Exception:
        try:
            # Find generated transcripts
            generated_transcripts = [trans for trans in transcript_list if trans.is_generated]
            if not generated_transcripts:
                return "No generated transcripts available."
            transcript = generated_transcripts[0]
        except Exception as e:
            return f"No suitable transcript found: {e}"
    
    try:
        # Fetch the English translation of the transcript
        english_transcript = transcript.translate('en')
        transcript_for_translation = " ".join([part['text'] for part in english_transcript.fetch()])
    except Exception as e:
        return f"Error fetching English translated transcript text: {e}"
    
    return transcript_for_translation

# Function to generate summary using Gemini
def generate_summary(transcript, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f'Generate a precise summary from the following text: {transcript}')
    return response.text

# Streamlit UI
st.title("Video Summarizer")

# Textbox to enter Gemini API key
api_key = st.text_input("Enter your Gemini API Key", type="password")

if api_key:
    # Upload a video file or enter a YouTube URL
    option = st.selectbox("Choose an input method", ("Upload a Video File", "Enter a YouTube URL"))

    if option == "Upload a Video File":
        uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])
        if uploaded_file is not None:
            # Extract and save the audio from the uploaded video
            audio_path = "extracted_audio.wav"
            extract_audio_from_video(uploaded_file, audio_path)
            
            # Convert the audio to text
            transcript = audio_to_text(audio_path)
            
            # Display the transcript
            st.write("Transcript extracted successfully:")
            st.write(transcript)
            
            # Generate and display the summary
            if st.button("Generate Summary"):
                summary = generate_summary(transcript, api_key)
                st.write("Summary:")
                st.write(summary)

    elif option == "Enter a YouTube URL":
        yt_url = st.text_input("Enter the YouTube URL")
        if yt_url:
            # Get the transcript from the YouTube video
            transcript = get_transcript(yt_url)
            
            # Display the transcript
            st.write("Transcript extracted successfully:")
            st.write(transcript)
            
            # Generate and display the summary
            if st.button("Generate Summary"):
                summary = generate_summary(transcript, api_key)
                st.write("Summary:")
                st.write(summary)
else:
    st.warning("Please enter your Gemini API key to proceed.")
