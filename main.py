from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_anthropic import ChatAnthropic
from tavily import TavilyClient
import os
load_dotenv()

tavily_client = TavilyClient()

@tool
def search(query: str) -> str:
    """Search the web for information"""
    response = tavily_client.search(query)
    return response

llm = ChatAnthropic(model="claude-sonnet-5")
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="What is the weather in Tokyo?")]})
    print(result)

if __name__ == "__main__":
    main()
