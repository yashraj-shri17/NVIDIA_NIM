# 📄 Resume GPT

Resume GPT is an interactive **Streamlit application** that leverages **LangChain**, **NVIDIA AI Endpoints**, and **FAISS** to help users query their resumes.  
It allows you to upload resumes in PDF format, embed them into a vector store, and ask natural language questions to get contextual answers.

---

## 🚀 Features

- 📤 **PDF Resume Upload** - Upload resumes in PDF format and automatically load them
- 🤖 **NVIDIA AI Integration** - Uses **NVIDIA LLM (`meta/llama3-8b-instruct`)** for generating responses
- 🔍 **Semantic Search** - **FAISS Vector Store** for efficient semantic search and retrieval
- 📝 **Smart Text Processing** - **Recursive Text Splitting** for breaking down long resumes into smaller chunks
- 🎨 **User-Friendly Interface** - Clean **Streamlit interface** for asking questions
- 📑 **Source Tracking** - Displays **source documents** used for generating answers

---

## 📂 Project Structure

```
.
├── resume/                # Folder containing your PDF resumes
├── .env                   # Environment file (store your NVIDIA_API_KEY here)
├── app.py                 # Main Streamlit app
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/resume-gpt.git
cd resume-gpt
```

### 2. Create and activate a virtual environment (recommended)
```bash
# For Linux/Mac
python -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root directory and add your NVIDIA API Key:
```env
NVIDIA_API_KEY=your_api_key_here
```

---

## ▶️ Usage

1. **Place your resume(s)** in the `resume/` directory (PDF format)
2. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```
3. **Open the local URL** shown in your terminal (default: `http://localhost:8501`)
4. **Ask questions** about your resume in the input box
5. **View the AI-generated answers** and their supporting source documents

---

## 📦 Requirements

The main dependencies include:
- `streamlit`
- `langchain`
- `langchain-community`
- `langchain-nvidia-ai-endpoints`
- `faiss-cpu`
- `python-dotenv`

See `requirements.txt` for complete list.

---

## 📸 Example

**User Question:**
> "How many projects on llm has been done by Yashraj Shrivastava"

**AI Response:**
> "Yashraj Shrivastava has done 2 projects on LLMs using LangChain, FAISS, and NVIDIA AI Endpoints etc."

---

## 📜 License

This project is licensed under the **MIT License**.