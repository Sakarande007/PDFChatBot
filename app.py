import streamlit as st
import google.generativeai as genai
from pdf_processor import PDFProcessor
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    st.error("Please set your GOOGLE_API_KEY in the .env file")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

# Initialize session state
if 'pdf_processor' not in st.session_state:
    st.session_state.pdf_processor = PDFProcessor()
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def initialize_model():
    """Initialize the Gemini model."""
    model = genai.GenerativeModel('gemini-2.0-flash-lite')
    return model

def get_gemini_response(prompt: str, context: str) -> str:
    """Get response from Gemini API."""
    try:
        model = initialize_model()
        full_prompt = f"""Context from PDFs:
{context}

User Question: {prompt}

Please provide a detailed answer based on the context provided. If the answer cannot be found in the context, please say so."""
        
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error getting response: {str(e)}"

# Streamlit UI
st.title("📚 Multi-PDF Chatbot")
st.write("Upload multiple PDFs and ask questions about their content!")

# File uploader
uploaded_files = st.file_uploader("Upload PDF files", type=['pdf'], accept_multiple_files=True)

# Process uploaded files
if uploaded_files:
    for uploaded_file in uploaded_files:
        if uploaded_file.name not in st.session_state.pdf_processor.get_pdf_names():
            with st.spinner(f"Processing {uploaded_file.name}..."):
                st.session_state.pdf_processor.process_pdf(uploaded_file, uploaded_file.name)
                st.success(f"Processed {uploaded_file.name}")

# Display processed PDFs
if st.session_state.pdf_processor.get_pdf_names():
    st.subheader("Processed PDFs:")
    for pdf_name in st.session_state.pdf_processor.get_pdf_names():
        st.write(f"📄 {pdf_name}")

# Chat interface
st.subheader("Chat with your PDFs")
user_question = st.text_input("Ask a question about your PDFs:")

if user_question:
    if not st.session_state.pdf_processor.get_pdf_names():
        st.warning("Please upload at least one PDF file first!")
    else:
        with st.spinner("Thinking..."):
            # Get context from all PDFs
            context = st.session_state.pdf_processor.get_all_content()
            
            # Get response from Gemini
            response = get_gemini_response(user_question, context)
            
            # Update chat history
            st.session_state.chat_history.append({"question": user_question, "answer": response})

# Display chat history
if st.session_state.chat_history:
    st.subheader("Chat History")
    for chat in st.session_state.chat_history:
        st.write("Q:", chat["question"])
        st.write("A:", chat["answer"])
        st.write("---")

# Clear button
if st.button("Clear Chat History"):
    st.session_state.chat_history = []
    st.session_state.pdf_processor.clear()
    st.experimental_rerun()
