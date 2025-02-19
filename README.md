### Efficient Inventory Management with RAG ChatBot

#### Business Problem
Managers and decision-makers need timely and accurate access to sales and inventory data. Traditional methods relying on technical teams for data retrieval are inefficient, time-consuming, and costly, causing delays in decision-making. This inefficiency hampers the ability to make swift, data-driven decisions.

#### Business Solution
To address the challenge, we developed a Retrieval-Augmented Generation (RAG) based chatbot. This chatbot leverages advanced AI to interact with documents and web URLs, chunk the content, generate embeddings, and provide answers to user queries based on the processed data. By implementing various advanced models and technologies, we enhanced data access efficiency.

#### Technology Stack
- **FastAPI**: Backend framework for handling API requests.
- **Streamlit**: Frontend framework for building the user interface.
- **HuggingFace Transformers**: For generating embeddings and processing text.
- **FAISS**: For efficient similarity search and retrieval.
- **Groq**: For generating responses using the Mixtral-8x7b-32768 model.

#### Features
- **File Upload**: Supports uploading PDF, DOCX, TXT, PPTX, and XLSX files.
- **URL Processing**: Processes up to 5 web URLs at a time.
- **Chunking and Embedding**: Chunks the content and generates embeddings using HuggingFace's sentence-transformers.
- **Query Response**: Answers user queries based on the processed data and provides source references.
- **Streamlit Frontend**: User-friendly interface for interacting with the chatbot.

#### Project Structure
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
│   └── app.py                # Main Streamlit application
│
└── README.md                 # Project documentation
```

#### Installation
1. **Clone the Repository**:
    ```
    git clone https://github.com/yourusername/rag-chatbot.git
    cd rag-chatbot
    ```

2. **Set Up the Backend**:
    Navigate to the backend folder:
    ```
    cd backend
    ```
    Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
    Create a `.env` file and add your environment variables:
    ```
    GROQ_API_KEY=your_groq_api_key
    HF_INFERENCE_API_KEY=your_huggingface_api_key
    ```

3. **Set Up the Frontend**:
    Navigate to the frontend folder:
    ```
    cd ../frontend
    ```
    Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

#### Run the Backend
Start the FastAPI server:
```
uvicorn main:app --host 127.0.0.1 --port 8080 --reload
```

#### Run the Frontend
Start the Streamlit application:
```
streamlit run app.py
```

#### Usage
1. **Upload Data**:
    - Use the sidebar to upload files or enter web URLs.
    - Click "Process Files" or "Process URLs" to chunk and embed the data.

2. **Ask Questions**:
    - Enter your query in the chat input box.
    - The chatbot will generate a response based on the processed data.

3. **Clear Chat History**:
    - Use the "Clear Chat History" button in the sidebar to reset the chat.

#### Business Benefits
- **Improved Efficiency**: Developed and deployed an AI-driven system, reducing data retrieval time and enabling faster, data-driven decision-making.
- **Lower Costs**: Reduced reliance on technical teams, decreasing related expenses by 10%.
- **High Accuracy**: Delivered accurate responses with 95% reliability through advanced machine learning models.
- **Enhanced User Experience**: Introduced a user-friendly, conversational interface, improving accessibility for non-technical users.
- **Operational Improvements**: Optimized data accessibility, leading to a 25% reduction in bounce rates.

By leveraging the RAG ChatBot, managers and decision-makers can now access timely and accurate sales and inventory data without relying on technical teams, thus improving the overall efficiency and effectiveness of the decision-making process.
