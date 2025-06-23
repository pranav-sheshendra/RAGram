from langchain.tools.tavily_search import TavilySearchResults
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

search_tool = TavilySearchResults(k=3)
results = search_tool.run("What is the capital of France?")
for i, r in enumerate(results, 1):
    print(f"{i}. {r['content']}")
