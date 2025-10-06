
# RAGr@m - A Web-Connected RAG Framework

RAGr@m is a lightweight, interactive Retrieval-Augmented Generation (RAG) application built using Streamlit and powered by **LLaMA 3** through **LangChain** and **Groq API**. It performs live web search using **Tavily** to provide up-to-date, contextually grounded answers.

## Features

-  **Real-Time Web Search** using Tavily API  
-  **Language Understanding** powered by LLaMA 3 via Groq  
-  **Retrieval-Augmented Generation (RAG)** pipeline  
-  **Source Transparency** — shows content used to answer  

## Dependencies

```bash
pip install streamlit langchain langchain-groq python-dotenv

```
## Environment Variables

Create a `.env` file in your project root with the following content:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## How It Works

1. User inputs a query in the Streamlit app.
2. Tavily performs a live web search and returns top results.
3. Extracted content is sent as **context** to the LLM.
4. The LLM generates a concise and accurate answer.
5. Both the answer and source content are displayed.

## 📄 License

This project is open-source and free to use under the MIT License.

