# Multi-PDF Chatbot with Gemini API

This is a Streamlit-based chatbot application that allows you to upload multiple PDF files and ask questions about their content using Google's Gemini API.

## Features

- Upload multiple PDF files
- Process and extract text from PDFs
- Chat interface to ask questions about the PDF content
- Chat history tracking
- Clear chat history and uploaded PDFs

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
   You can get your API key from the [Google AI Studio](https://makersuite.google.com/app/apikey)

## Running the Application

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

## Usage

1. Upload one or more PDF files using the file uploader
2. Wait for the PDFs to be processed
3. Type your question in the chat interface
4. View the response and chat history
5. Use the "Clear Chat History" button to start fresh

## Requirements

- Python 3.7+
- Streamlit
- Google Generative AI (Gemini)
- PyPDF2
- python-dotenv

## Note

Make sure your PDFs are text-based and not scanned images, as the current version doesn't support OCR. 