import streamlit as st
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.tools import tool
from langchain_core.documents import Document
from langgraph.prebuilt import create_react_agent

load_dotenv()

model = init_chat_model("openai:gpt-4o-mini")

# Define mental health tools
@tool
def store_personal_reflection(title: str, content: str) -> str:
    """Store a personal reflection or thought in the vector database."""
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    doc = Document(page_content=content, metadata={"title": title})
    vectorstore.add_documents([doc])
    vectorstore.persist()
    return f"Stored reflection: {title}"

@tool
def retrieve_supportive_notes(query: str) -> str:
    """Retrieve supportive notes or past reflections from the vector database."""
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    docs = vectorstore.similarity_search(query, k=5)
    return "\n\n".join([f"Title: {doc.metadata['title']}\nContent: {doc.page_content}" for doc in docs])

tools = [store_personal_reflection, retrieve_supportive_notes]

agent = create_react_agent(
    model=model,
    tools=tools,
    prompt="You are a mental health companion agent. Your goal is to provide supportive, empathetic, and helpful responses to assist users with mental health and emotional well-being. Offer encouragement, listen actively, and suggest positive coping strategies."
)

def generate_response(prompt):
    inputs = {"messages": [{"role": "user", "content": prompt}]}
    response_text = ""
    for chunk in agent.stream(inputs, stream_mode="updates"):
        if 'agent' in chunk:
            message = chunk['agent']['messages'][-1]
            response_text += message.content
            yield message.content
    return response_text

st.title("Mental Health Companion Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Share how you're feeling or ask for support..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_generator = generate_response(prompt)
        response = st.write_stream(response_generator)
    st.session_state.messages.append({"role": "assistant", "content": response})
