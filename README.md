# 📄 DocBot — Ask Questions From Any Documentation

DocBot is an intelligent chatbot that allows you to load **any documentation URL** and ask natural language questions about it. Powered by Google's **Gemini API**, **Agnos agentic framework**, and **LanceDB vector search**, it converts documentation into an interactive, AI-powered Q&A interface.

---

## 🚀 Features

- 🌐 Load and index documentation from any URL
- 🤖 Ask questions in natural language
- 🧠 Uses Gemini embeddings for semantic understanding
- 🔍 Hybrid search with LanceDB
- 📝 Maintains chat history
- 📦 Fully built using [Streamlit](https://streamlit.io)

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – UI Framework
- **Agnos** – Agent framework
- **Gemini API** – LLM & Embedding Model
- **LanceDB** – Vector database
- **SQLite** – Session & memory storage

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/docbot.git
cd docbot
pip install -r requirements.txt
````

Make sure to set your **Google API Key** in the code:

```python
api_key = "YOUR_API_KEY"
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📄 Example Usage

1. Paste a documentation URL (e.g., `https://docs.python.org/3/library/functions.html`)
2. Click **Load & Index Documentation**
3. Ask questions like:

   * “What does the `map()` function do?”
   * “How do I use `filter()` in Python?”

---

## 🔒 Disclaimer

This app relies on Gemini API and external documentation. Accuracy depends on the content of the provided docs. Make sure to not expose any private or sensitive data in public deployments.

---

## 🧠 License

MIT License. Open to contributions!

<img width="1383" alt="Screenshot 2025-06-11 at 6 14 28 PM" src="https://github.com/user-attachments/assets/cd299fed-5d64-47aa-95dd-1862b030515c" />

```


