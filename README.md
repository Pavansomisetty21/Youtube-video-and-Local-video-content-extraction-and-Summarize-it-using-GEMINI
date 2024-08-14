# Youtube-video-and-Local-video-content-extraction-and-Summarize-it-using-GEMINI
In this we have done that extraction of transcription(data) from youtube video and summarize it and In case of Local video we extract audio from video later it will be transformed to text to summarize

# Video and YouTube Transcript Summarizer with Streamlit

## Overview
This project is a web-based application built using Streamlit that allows users to summarize the content of videos and YouTube videos. The app extracts transcripts from video files or YouTube URLs and generates concise summaries using Google's Gemini AI API. Users can interact with the application by uploading video files, entering YouTube URLs, and providing their Gemini API key to leverage the AI-powered summarization capabilities.


## How It Works

### 1. Extracting Audio from Video Files
   - When a user uploads a video file (e.g., MP4, AVI, MOV), the app utilizes the `MoviePy` library to extract the audio track from the video. This audio is saved as a WAV file, which is then used for speech-to-text conversion.
   - The extraction process is efficient and works with most common video formats, ensuring that users can process various types of videos.

### 2. Converting Audio to Text
   - The app employs the `SpeechRecognition` library to convert the extracted audio file into text. This process involves:
     - **Loading the Audio**: The WAV file is loaded into the `SpeechRecognition` engine.
     - **Recognizing Speech**: The audio is processed to recognize speech and generate a textual transcript. The Google Web Speech API is used for this purpose, providing accurate transcription of spoken words.
   - The resulting transcript captures the spoken content of the video, which is then passed on for summarization.

### 3. Fetching YouTube Transcripts
   - For YouTube videos, users can input a YouTube URL. The app uses the `YouTubeTranscriptApi` to retrieve the video's transcript. The process involves:
     - **Extracting the Video ID**: The app parses the provided YouTube URL to extract the video ID, which is needed to request the transcript.
     - **Retrieving Transcripts**: The app first tries to fetch manually created transcripts. If unavailable, it falls back on automatically generated transcripts provided by YouTube.
     - **Translation**: If the transcript is not in English, the app can translate it into English using the transcript API’s built-in translation capabilities.
   - This approach allows users to work with a wide range of YouTube content, regardless of the language of the original transcript.

### 4. Generating Summaries with Gemini AI
   - The textual transcript, whether extracted from a video file or fetched from YouTube, is passed to the Gemini AI for summarization. The app uses Google's Gemini API for this task:
     - **Text Processing**: The transcript is formatted into a prompt that asks the Gemini AI to generate a precise summary.
     - **Summary Generation**: The Gemini AI processes the transcript and generates a concise summary that captures the essential points of the video content.
     - **Displaying the Summary**: The generated summary is displayed in the Streamlit interface, providing users with a quick and informative overview of the video's content.
   - This step leverages the advanced natural language understanding capabilities of Gemini AI to produce high-quality summaries.

### 5. Streamlit Interface
   - The entire process is wrapped in a user-friendly Streamlit interface, which includes:
     - **File Upload**: Users can upload their video files directly through the app.
     - **URL Input**: Users can enter YouTube URLs to fetch and summarize transcripts.
     - **API Key Input**: A secure textbox allows users to input their Gemini API key, enabling the summarization features.
     - **Results Display**: The app presents the transcript and the generated summary in a clear and organized manner, making it easy for users to read and use the information.
   - The Streamlit interface is designed to be intuitive and accessible, allowing even non-technical users to utilize the app effectively.


## Features
- **Video File Processing**: Users can upload video files (e.g., MP4, AVI, MOV), and the app extracts the audio, converts it to text, and generates a summary of the content.
- **YouTube Video Summarization**: Users can input a YouTube video URL, and the app retrieves the transcript (including translated versions if available), then summarizes the content using AI.
- **Gemini AI Integration**: The app utilizes the Gemini API to generate high-quality, precise summaries from the extracted transcripts.
- **User-Friendly Interface**: Streamlit provides an intuitive and easy-to-use interface for users, including options to input a Gemini API key securely and choose between video file upload or YouTube URL input.

## Technical Details
- **Audio Extraction**: The app uses `MoviePy` to extract audio from video files.
- **Speech Recognition**: The app employs `SpeechRecognition` to convert audio to text.
- **YouTube Transcript Retrieval**: The app uses `YouTubeTranscriptApi` to fetch transcripts from YouTube videos, with options for translation.
- **AI-Powered Summarization**: Integrated with the Google Gemini API, the app generates concise summaries from the extracted or fetched transcripts.
- **Streamlit Integration**: The entire process is wrapped in a Streamlit app, making it accessible through a web interface where users can easily upload files, input URLs, and view results.

## Usage
1. **API Key Input**: Users need to enter their Gemini API key into the provided textbox in the app.
2. **Video File Summarization**:
   - Users can upload a video file directly through the app.
   - The app extracts the audio, converts it to text, and provides a transcript.
   - A summary is generated and displayed.
3. **YouTube Video Summarization**:
   - Users can enter a YouTube video URL.
   - The app fetches the transcript, translates it if necessary, and generates a summary.
   - The transcript and summary are displayed in the app.

## Potential Use Cases
- **Content Creators**: Quickly summarize video content to create descriptions, notes, or synopses.
- **Researchers**: Summarize long video lectures or presentations for quick reference.
- **Marketers**: Extract key points from promotional videos for summaries or taglines.
- **Educators**: Generate summaries of educational videos for quick review or study guides.

## Prerequisites
- Python 3.x
- Required Python libraries: `streamlit`, `moviepy`, `speechrecognition`, `youtube_transcript_api`, `google-generativeai`
- Google Gemini API key

## Conclusion
This project showcases how AI and video processing can be combined to create a powerful tool for generating concise, informative summaries from video content, providing a valuable resource for content creators, educators, and professionals across various industries.
