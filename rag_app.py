import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq  # FREE Llama 3 model

# ===========================
# 1. Load PDF
# ===========================
loader = PyPDFLoader(
        "ai-ml-fresher.pdf"
)
documents = loader.load()

# ===========================
# 2. Split into chunks
# ===========================
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(documents)

# ===========================
# 3. Create FREE embeddings
# ===========================
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)  # free, lightweight, fast

# ===========================
# 4. Create vector DB
# ===========================
vectordb = Chroma.from_documents(chunks, embeddings)

# ===========================
# 5. Create retriever
# ===========================
retriever = vectordb.as_retriever()

# ===========================
# 6. FREE LLM using Groq (Llama 3)
# ===========================
api_key = os.environ.get("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")
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=api_key
)

# ===========================
# 7. Create RAG pipeline
# ===========================
rag = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

# ===========================
# 8. Ask questions
# ===========================
while True:
    query = input("\nAsk something from your PDF: ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    response = rag.invoke({"query": query})
    print("\nAnswer:", response["result"])

