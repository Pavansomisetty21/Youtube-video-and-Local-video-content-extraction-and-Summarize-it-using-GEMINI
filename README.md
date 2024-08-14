# Youtube-video-and-Local-video-content-extraction-and-Summarize-it-using-GEMINI
In this we have done that extraction of transcription(data) from youtube video and summarize it and In case of Local video we extract audio from video later it will be transformed to text to summarize

# Video and YouTube Transcript Summarizer with Streamlit

## Overview
This project is a web-based application built using Streamlit that allows users to summarize the content of videos and YouTube videos. The app extracts transcripts from video files or YouTube URLs and generates concise summaries using Google's Gemini AI API. Users can interact with the application by uploading video files, entering YouTube URLs, and providing their Gemini API key to leverage the AI-powered summarization capabilities.

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
