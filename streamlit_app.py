import os
import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq

st.title("PDF QA with RAG")


@st.cache_resource
def load_rag():

    st.write("Loading PDF...")

    loader = PyPDFLoader(
        "ai-ml-fresher.pdf"
    )
    documents = loader.load()

    st.write("Splitting PDF...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    st.write("Loading embeddings model...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    st.write("Creating vector database...")

    vectordb = Chroma.from_documents(
        chunks,
        embeddings
    )

    st.write("Creating retriever...")

    retriever = vectordb.as_retriever()

    st.write("Loading Groq LLM...")

    api_key = os.environ.get("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")

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        groq_api_key=api_key
    )

    st.write("Building RAG pipeline...")

    rag = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    st.write("RAG Ready ✅")

    return rag


with st.spinner("Loading PDF and AI model..."):
    rag = load_rag()

query = st.text_input("Ask something from your PDF:")

if query:
    with st.spinner("Generating answer..."):
        response = rag.invoke({"query": query})
        st.write(response["result"])
