📄 PDF Question Answering with RAG (Retrieval-Augmented Generation)

Ask questions from any PDF using free AI — powered by LangChain, Groq (Llama 3), and HuggingFace Embeddings.


🧠 What is this project?
This project lets you chat with any PDF file using a RAG (Retrieval-Augmented Generation) pipeline. Instead of a generic AI answer, the model searches your actual document and gives you accurate, context-aware responses grounded in the PDF content.
It comes in two flavors:

ragg_app.py — Terminal-based CLI interface
streamlit_app.py — Beautiful web UI using Streamlit


🏗️ Architecture Overview
PDF File
   ↓
PyPDFLoader          ← Loads and parses the PDF
   ↓
RecursiveCharacterTextSplitter  ← Splits into 500-char chunks
   ↓
HuggingFace Embeddings          ← Converts chunks to vectors (free, local)
(all-MiniLM-L6-v2)
   ↓
ChromaDB Vector Store           ← Stores & indexes the vectors
   ↓
Retriever                       ← Fetches top relevant chunks for a query
   ↓
Groq LLM (Llama 3.1 8B)        ← Free, fast LLM via Groq API
   ↓
RetrievalQA Chain               ← Combines retriever + LLM
   ↓
Answer ✅

✨ Features

📂 Load and parse any PDF document
🔍 Semantic search using vector embeddings
🤖 Free LLM via Groq API (Llama 3.1 8B Instant)
💾 Local vector storage with ChromaDB (no paid DB needed)
🖥️ CLI mode for quick usage
🌐 Web UI mode via Streamlit
⚡ Fast inference — Groq delivers near-instant responses
💸 Completely free to run (no OpenAI key needed)


🛠️ Tech Stack
ComponentTool / LibraryPDF Loadinglangchain-community → PyPDFLoaderText SplittingRecursiveCharacterTextSplitterEmbeddingsHuggingFaceEmbeddings (MiniLM-L6-v2)Vector StoreChromaDBLLMGroq → llama-3.1-8b-instantRAG ChainLangChain → RetrievalQAWeb UIStreamlit

📦 Installation
1. Clone the repository
bashgit clone https://github.com/your-username/pdf-rag-qa.git
cd pdf-rag-qa
2. Create a virtual environment (recommended)
bashpython -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
3. Install dependencies
bashpip install -r requirements.txt
4. Set your Groq API key
Get your free API key from https://console.groq.com/
bash# Linux / macOS
export GROQ_API_KEY="your_api_key_here"

# Windows (CMD)
set GROQ_API_KEY=your_api_key_here

# Windows (PowerShell)
$env:GROQ_API_KEY="your_api_key_here"

🚀 Usage
Option 1 — Terminal (CLI)
bashpython ragg_app.py
Then type your question:
Ask something from your PDF: What is the candidate's experience with Python?

Answer: The candidate has 1 year of experience with Python and has worked on...
Type exit to quit.

Option 2 — Web UI (Streamlit)
bashstreamlit run streamlit_app.py
Opens a browser window at http://localhost:8501 where you can type questions and get answers interactively.

⚙️ Configuration
To use your own PDF, update the file path in both scripts:
pythonloader = PyPDFLoader("path/to/your/file.pdf")
You can also tune these parameters for better results:
python# In the splitter
chunk_size=500,       # Increase for more context per chunk
chunk_overlap=50      # Increase to avoid missing info at chunk boundaries

📁 Project Structure
pdf-rag-qa/
│
├── ragg_app.py          # CLI version of the RAG app
├── streamlit_app.py     # Web UI version using Streamlit
├── requirements.txt     # All Python dependencies
└── README.md            # You're reading this!

📋 Requirements
Create a requirements.txt with:
langchain
langchain-community
langchain-groq
chromadb
sentence-transformers
huggingface-hub
pypdf
streamlit

🔐 Environment Variables
VariableDescriptionGROQ_API_KEYYour Groq API key (free at console.groq.com)

💡 How RAG Works (Simple Explanation)
Traditional AI doesn't know what's in your PDF. RAG solves this by:

Splitting your PDF into small text chunks
Converting each chunk into a vector (a list of numbers capturing meaning)
Storing these vectors in a database (ChromaDB)
When you ask a question, finding the most relevant chunks
Feeding those chunks + your question to the LLM
The LLM generates an answer based on your document, not just its training data


🙋 FAQ
Q: Do I need to pay for anything?
No. Groq API has a free tier, and HuggingFace embeddings run locally for free.
Q: Can I use a different PDF?
Yes! Just change the file path in the script.
Q: Can I swap the LLM?
Yes. You can replace ChatGroq with any LangChain-compatible LLM (OpenAI, Ollama, etc.).
Q: Does it work on large PDFs?
Yes, but processing time increases with file size. The first load may take a minute.

📄 License
MIT License — feel free to use, modify, and distribute.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.

👨‍💻 Author
Built with ❤️ using LangChain + Groq + Streamlit
