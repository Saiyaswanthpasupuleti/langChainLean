# import the necessary libraries
from dotenv import load_dotenv
import os
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from tavily import TavilyClient




# load the environment variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

tavily=TavilyClient(api_key=tavily_api_key)


# create the tools
def search(query:str)->str:
    """
    Search the web for the query
    Args:
        query: The query to search for
    Returns:
        The search results
    """
    print(f"Searching the web for {query}")
    return tavily.search(query)




# create the llm
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
tool=[search]

agent = create_agent(model=llm, tools=tool)


# Runnable 
responce= agent.invoke({"messages":HumanMessage(content="What is the weather in Hyderabad?")})
print(responce)