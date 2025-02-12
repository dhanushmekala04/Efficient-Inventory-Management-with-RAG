# RAG ChatBot

## Overview

The RAG ChatBot is a Retrieval-Augmented Generation (RAG) based chatbot that allows users to interact with documents and web URLs. It processes uploaded files or URLs, chunks the content, generates embeddings, and provides answers to user queries based on the processed data. The backend is built using FastAPI, and the frontend is a Streamlit application.

## Features

- **File Upload**: Supports uploading PDF, DOCX, TXT, PPTX, and XLSX files.
- **URL Processing**: Processes up to 5 web URLs at a time.
- **Chunking and Embedding**: Chunks the content and generates embeddings using HuggingFace's sentence-transformers.
- **Query Response**: Answers user queries based on the processed data and provides source references.
- **Streamlit Frontend**: User-friendly interface for interacting with the chatbot.

## Project Structure

```
project/
│
├── backend/
│   ├── main.py               # FastAPI backend application
│   ├── .env                  # Environment variables
│   └── requirements.txt      # Python dependencies
│
├── frontend/
│   ├── home_page.py          # Streamlit frontend application
│   └── app.py               # Main Streamlit application
│
└── README.md                 # Project documentation
```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/rag-chatbot.git
   cd rag-chatbot
   ```

2. **Set Up the Backend**:
   - Navigate to the `backend` folder:
     ```bash
     cd backend
     ```
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Create a `.env` file and add your environment variables:
     ```plaintext
     GROQ_API_KEY=your_groq_api_key
     HF_INFERENCE_API_KEY=your_huggingface_api_key
     ```

3. **Set Up the Frontend**:
   - Navigate to the `frontend` folder:
     ```bash
     cd ../frontend
     ```
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the Backend**:
   - Start the FastAPI server:
     ```bash
     uvicorn main:app --host 127.0.0.1 --port 8080 --reload
     ```

5. **Run the Frontend**:
   - Start the Streamlit application:
     ```bash
     streamlit run app.py
     ```

## Usage

1. **Upload Data**:
   - Use the sidebar to upload files or enter web URLs.
   - Click "Process Files" or "Process URLs" to chunk and embed the data.

2. **Ask Questions**:
   - Enter your query in the chat input box.
   - The chatbot will generate a response based on the processed data.

3. **Clear Chat History**:
   - Use the "Clear Chat History" button in the sidebar to reset the chat.

## Technologies Used

- **FastAPI**: Backend framework for handling API requests.
- **Streamlit**: Frontend framework for building the user interface.
- **HuggingFace Transformers**: For generating embeddings and processing text.
- **FAISS**: For efficient similarity search and retrieval.
- **Groq**: For generating responses using the Mixtral-8x7b-32768 model.


## Acknowledgments

- [HuggingFace](https://huggingface.co/) for the transformers and embeddings.
- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework.
- [Streamlit](https://streamlit.io/) for the frontend framework.

## Contact

For any questions or feedback, please open an issue on GitHub or contact the maintainer directly.

---

Enjoy using the RAG ChatBot! 🚀


+-------------------+
|  RAG Chatbot      |
+-------------------+
        |
        |
+-------v-------+
|  Frontend     |
+-------+-------+
        |
+-------v-------+
| Streamlit UI  |
+-------+-------+
        |
+-------v-------+
| Chat Interface|
+-------+-------+
        |
+-------v-------+
| Query Input   |
+-------+-------+
        |
+-------v-------+
| Response Display|
+-------+-------+
        |
+-------v-------+
| Source References|
+---------------+

+-------------------+
|  Backend          |
+-------+-------+
        |
+-------v-------+
| FastAPI Server|
+-------+-------+
        |
+-------v-------+
| Document Processing|
+-------+-------+
        |
+-------v-------+
| Embedding Storage|
+-------+-------+
        |
+-------v-------+
| Query Processing|
+-------+-------+
        |
+-------v-------+
| Response Generation|
+---------------+

+-------------------+
|  Vector Database  |
+-------+-------+
        |
+-------v-------+
| FAISS/Pinecone|
+---------------+

+-------------------+
|  LLM Integration  |
+-------+-------+
        |
+-------v-------+
| Groq/OpenAI API|
+---------------+
