import streamlit as st
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.yfinance import YFinanceTools
from agno.embedder.google import GeminiEmbedder
from agno.knowledge.url import UrlKnowledge
from agno.storage.sqlite import SqliteStorage
from agno.vectordb.lancedb import LanceDb, SearchType
import re

def strip_markdown(text):
    
    text = re.sub(r"```(?:\w+)?", "", text)
    
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    
    text = re.sub(r"`(.*?)`", r"\1", text)
    return text.strip()


api_key = "YOUR_GEMINI_API_KEY"  

st.set_page_config(page_title="DocBot 💬", layout="wide")

st.title("📄 DocBot — Ask Questions From Any Documentation")

user_url = st.text_input("Enter the documentation URL", placeholder="https://example.com/docs")

if "agent" not in st.session_state:
    st.session_state.agent = None
    st.session_state.history = []

if st.button("🔄 Load & Index Documentation") and user_url:
    with st.spinner("Loading and indexing documentation..."):
        knowledge = UrlKnowledge(
                urls=[user_url],
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="dynamic_docs",
        search_type=SearchType.hybrid,
        embedder=GeminiEmbedder(
    id="embedding-001",  
    api_key=api_key,
)
            ),
        )
        storage = SqliteStorage(table_name="agent_sessions", db_file="tmp/agent.db")

        st.session_state.agent = Agent(
            model=Gemini(
        id="gemini-2.0-flash",
        api_key=api_key,          
    ),
    tools=[],
    instructions=[
       "Search the loaded documentation before answering.",
        "Do not hallucinate. Only answer from the provided document.",
    ],
    knowledge=knowledge,
    storage=storage,
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_runs=3,
    markdown=True,
        )
        st.session_state.agent.knowledge.load(recreate=True)
    st.success("✅ Documentation loaded successfully. You can start asking questions!")


if st.session_state.agent:
    user_input = st.text_input("❓ Ask a question", key="user_question")

if st.button("💬 Get Answer") and user_input:
    with st.spinner("Thinking..."):
        answer = st.session_state.agent.run(user_input)
        
        
        response_text = answer.content if hasattr(answer, "content") else str(answer)
        cleaned_response = strip_markdown(response_text)

        st.session_state.history.append((user_input, cleaned_response))
        st.text(f"You: {user_input}")

        st.text(f"Bot: {response_text}")


    if st.session_state.history:
        with st.expander("🕘 View Chat History"):
            for q, a in st.session_state.history:
                st.markdown(f"You: {q}")
                st.markdown(f"Bot: {a}")

