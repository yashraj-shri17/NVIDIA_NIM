# 📄 Resume GPT

Resume GPT is an interactive **Streamlit application** that leverages **LangChain**, **NVIDIA AI Endpoints**, and **FAISS** to help users query their resumes.  
It allows you to upload resumes in PDF format, embed them into a vector store, and ask natural language questions to get contextual answers.

---

## 🚀 Features
- Upload resumes in PDF format and automatically load them.
- Uses **NVIDIA LLM (`meta/llama3-8b-instruct`)** for generating responses.
- **FAISS Vector Store** for efficient semantic search and retrieval.
- **Recursive Text Splitting** for breaking down long resumes into smaller chunks.
- User-friendly **Streamlit interface** for asking questions.
- Displays **source documents** used for generating answers.

---

## 📂 Project Structure
```

.
├── resume/                # Folder containing your PDF resumes
├── .env                   # Environment file (store your NVIDIA\_API\_KEY here)
├── app.py                 # Main Streamlit app
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

````

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/resume-gpt.git
   cd resume-gpt
````

2. **Create and activate a virtual environment** (recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory and add your NVIDIA API Key:

   ```
   NVIDIA_API_KEY=your_api_key_here
   ```

---

## ▶️ Usage

1. Place your resume(s) in the `resume/` directory (PDF format).
2. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```
3. Open the local URL shown in your terminal (default: `http://localhost:8501`).
4. Ask questions about your resume in the input box.
5. View the AI-generated answers and their supporting source documents.

---

## 📦 Requirements

Key dependencies:

* `streamlit`
* `langchain`
* `langchain-community`
* `langchain-nvidia-ai-endpoints`
* `faiss-cpu`
* `python-dotenv`

Full list is in `requirements.txt`.

---

## 📸 Example

**Ask:**
👉 "What are my key skills?"

**Answer:**
✅ "Your resume highlights skills in Python, Data Science, and Machine Learning."

---

## 💡 Future Improvements

* Support multiple resumes at once.
* Add authentication for secure access.
* Improve UI with advanced filtering and search options.

---

## 🤝 Contributing

Contributions are welcome! Please fork the repo and submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**.

---

