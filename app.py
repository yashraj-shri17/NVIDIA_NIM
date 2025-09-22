import streamlit as st
import os
import time
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings, ChatNVIDIA as CHATNVIDIA
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()
os.environ["NVIDIA_API_KEY"] = os.getenv("NVIDIA_API_KEY")

llm = CHATNVIDIA(model="meta/llama3-8b-instruct", temperature=0.5, max_retries=3)

# Initialize session state to avoid AttributeError
if "vectors" not in st.session_state:
    st.session_state.vectors = None

def vector_embedding():
    if st.session_state.vectors is None:
        st.session_state.embeddings = NVIDIAEmbeddings()
        st.session_state.loader = PyPDFDirectoryLoader("./resume")
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:30])
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

st.title("Resume GPT")

prompt = ChatPromptTemplate.from_template(
   """
   You are a helpful AI assistant that helps people find information about their resume.
   You are given the following extracted parts of a long resume and a question.
   Provide a conversational answer based on the context provided.
   If you don't know the answer, just say that you don't know, don't try to make
   <context>
   {context}
   </context>
   Question: {input}"""
)

prompt1 = st.text_input("Ask a question about your resume")

if st.button("Get Answer") and prompt1:
    vector_embedding()
    st.write("Generating answer...")

    document_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
    retriever = st.session_state.vectors.as_retriever(search_type="similarity", search_kwargs={"k":3})
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    start = time.process_time()
    response = retrieval_chain.invoke({"input": prompt1})
    st.write(f"Response time: {time.process_time() - start:.2f} seconds")
    st.write(response['answer'])

    with st.expander("Source Documents"):
        for i, doc in enumerate(response["context"]):
            st.write(f"Source Document {i+1}")
            st.write(doc.page_content)
            st.write("-----------------------")
