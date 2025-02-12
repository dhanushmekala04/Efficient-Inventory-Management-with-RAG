import os
import re
from typing import List
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException, UploadFile, Depends
from langchain_community.document_loaders import (
    TextLoader, PyPDFLoader, Docx2txtLoader, UnstructuredURLLoader,
    UnstructuredExcelLoader, UnstructuredPowerPointLoader
)
from langchain_groq.chat_models import ChatGroq


from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQAWithSourcesChain

# Load environment variables
load_dotenv()

# Validate GROQ API key
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY is missing from the .env file")

#DB_FAISS_PATH = "./vector"

app = FastAPI()

# Ensure tempDir exists
if not os.path.exists("tempDir"):
    os.makedirs("tempDir")
#

def chunk_data(data, chunk_size=256, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = text_splitter.split_documents(data)
    return chunks

# Create embeddings using HuggingFaceEmbeddings and save them in a FAISS vectordb
def create_embeddings(chunks):
   
    embeddings = HuggingFaceInferenceAPIEmbeddings(
    api_key=os.getenv("HF_INFERENCE_API_KEY"), model_name="sentence-transformers/all-MiniLM-l6-v2"
)
# Equivalent to SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(chunks, embeddings)
    #vector_store.save_local(DB_FAISS_PATH)
    return vector_store

# Endpoint to process files, chunk, and calculate embeddings
@app.post("/upload-files/")
async def upload_files(files: List[UploadFile]):
    global vector_store, num_chunks, processed_chunks

    all_documents = []
    
    # Save and process files
    for file in files:
        file_path = os.path.join("tempDir", file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        
        try:
            if file.filename.endswith(".pdf"):
                loader = PyPDFLoader(file_path)
            elif file.filename.endswith(".docx"):
                loader = Docx2txtLoader(file_path)
            elif file.filename.endswith(".txt"):
                loader = TextLoader(file_path, encoding='UTF-8')
            elif file.filename.endswith(".pptx"):
                loader = UnstructuredPowerPointLoader(file_path)
            elif file.filename.endswith(".xlsx"):
                loader = UnstructuredExcelLoader(file_path)
            else:
                raise HTTPException(status_code=400, detail=f"Unsupported file type: {file.filename}")

            documents = loader.load()
            all_documents.extend(documents)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing file {file.filename}: {str(e)}")
        
    # Chunk data
    chunks = chunk_data(all_documents)
    num_chunks = len(chunks)
    processed_chunks = chunks
    
    # Create embeddings and save them in FAISS vector store
    vector_store = create_embeddings(chunks)
    
    # Return the number of chunks
    return {"num_chunks": num_chunks}

# Endpoint to process URLs, chunk, and calculate embeddings
class URLInput(BaseModel):
    urls: List[str]

@app.post("/process-urls/")
async def process_urls(url_input: URLInput):
    global vector_store, num_chunks, processed_chunks

    urls = url_input.urls
    if len(urls) > 5:
        raise HTTPException(status_code=400, detail="You can only process up to 5 URLs at a time.")
    
    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()

    # Chunk data
    chunks = chunk_data(data)
    num_chunks = len(chunks)
    processed_chunks = chunks
    
    # Create embeddings and save them in FAISS vector store
    vector_store = create_embeddings(chunks)
    
    # Return the number of chunks
    return {"num_chunks": num_chunks}


# Endpoint to generate a response based on the user's query
class QueryRequest(BaseModel):
    query: str


@app.post("/generate-response/")
async def generate_response(query_request: QueryRequest):
    global vector_store, num_chunks, processed_chunks

    if vector_store is None:
        raise HTTPException(status_code=400, detail="Please upload and process your data (vector store is not created)")

    # Generating response with source file reference
    llm = ChatGroq(groq_api_key=groq_api_key, model_name="mixtral-8x7b-32768")
    retriever = vector_store.as_retriever(search_type='similarity', search_kwargs={'k': 10})
    chain = RetrievalQAWithSourcesChain.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

    ans = chain.invoke({"question": query_request.query})

    # Response text cleaning
    ans['sources'] = os.path.basename(ans['sources'])
    ans['answer'] = re.sub(r'\s*SOURCES:$', '', ans['answer'])

    return {
        "answer": ans['answer'],
        "sources": ans['sources'],
    }


# Run the FastAPI server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=1000, reload=True)
