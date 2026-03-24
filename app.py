import streamlit as st
import requests

# ---------------- Page config ----------------
st.set_page_config(
    page_title="Chatbot",
    layout="wide"
)

st.title("🤖Chatbot")
st.write("Powered by Ollama")

# ---------------- Session state ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- Sidebar ----------------
st.sidebar.title("Settings")
model = st.sidebar.selectbox(
    "Choose Model",
    ["qwen2.5:3b", "qwen3:1.7b"]  # Add more if installed
)

# ---------------- Tabs ----------------
tab_chat, tab_history = st.tabs(["💬 Chat", "📜 History"])

# ---------------- CHAT TAB ----------------
with tab_chat:
    # Display previous messages as chat bubbles
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input at bottom (auto-clears)
    if prompt := st.chat_input("Type your message..."):
        # Display user message immediately
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Call Ollama LLM
        with st.spinner("Bot is typing..."):
            try:
                response = requests.post(
                    "http://localhost:11434/api/generate",
                    json={
                        "model": model,
                        "prompt": prompt,
                        "stream": False
                    }
                )
                bot_response = response.json()["response"]
            except Exception as e:
                bot_response = f"⚠️ Error: {e}"

        # Display bot response
        st.chat_message("assistant").markdown(bot_response)
        st.session_state.messages.append({"role": "assistant", "content": bot_response})

    # Clear chat button
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.experimental_rerun()

# ---------------- HISTORY TAB ----------------
with tab_history:
    st.subheader("📜 Chat History")
    if st.session_state.messages:
        for msg in st.session_state.messages:
            st.markdown(f"**{msg['role'].capitalize()}:** {msg['content']}")
        
        # Optional: download chat history
        st.download_button(
            "Download Chat History",
            data="\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in st.session_state.messages]),
            file_name="chat_history.txt"
        )
    else:
        st.write("No history yet.")