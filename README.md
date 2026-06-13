# Local LLM Chatbot (Streamlit + Ollama)

This project is a **ChatGPT-style chatbot interface** built using **Streamlit**, connected to a **locally running LLM via Ollama**.  
It allows users to interact with a large language model on their own computer with a clean and interactive UI.

---

## Features
- ChatGPT-style chat interface with bubbles
- Conversation history panel (History Tab)
- Reset (Clear Chat) button
- Sidebar model selection (switch between `qwen2.5:3b` and `qwen3:1.7B`)
- Download chat history as a text file
- Smooth communication with the local LLM
- Spinner indicating “Bot is typing…”

---

## Requirements
- Python 3.x  
- Streamlit  
- Requests  
- Ollama (local LLM runner)  

---

## How to Run

1. **Install Python dependencies**:
pip install -r requirements.txt

2. Run the Ollama model locally:
ollama run qwen3:1.7B

3. Start the Streamlit app:
streamlit run app.py

4. Open the app in your browser:
It should open automatically, or go to:
http://localhost:8501
