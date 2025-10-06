#libraries
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv
import os
import time

# environment
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

st.image("anahata.png", width=150)
st.markdown("<h1 style='color: orange; text-align: center;'>🔱 RAGr@m</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='color: red; text-align: center;'>an ♾️ RAG frame</h4>", unsafe_allow_html=True)


llm = ChatGroq(groq_api_key=groq_api_key, model_name="openai/gpt-oss-120b")

# template format
prompt = ChatPromptTemplate.from_template(
    """
    Answer the question based on the following web context. 
    Be concise and accurate.

    <context>
    {context}
    </context>

    Question: {input}
    """
)

# question text
question = st.text_input("🧠 Ask a question (searched from the live web)")

# answer run
if question:
    with st.spinner("🔎 Searching the web and generating answer..."):
        start = time.process_time()

        # web search
        search_tool = TavilySearchResults(k=5)
        results = search_tool.run(question)

        documents = [doc["content"] for doc in results if "content" in doc]
        context = "\n\n".join(documents)

        # RAG answer
        chain = prompt | llm
        response = chain.invoke({"context": context, "input": question})

        st.write("🧠 **Answer:**", response.content)
        st.caption(f"⏱️ Took {time.process_time() - start:.2f}s")

        # source shown
        with st.expander("📄 Sources used"):
            for i, doc in enumerate(documents, 1):
                st.markdown(f"**Source {i}:**\n{doc}")
