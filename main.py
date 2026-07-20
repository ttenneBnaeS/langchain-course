from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_anthropic import ChatAnthropic
from langchain_tavily import TavilySearch
import os

load_dotenv()


class Source(BaseModel):
    name: str = Field(description="The name of the source")
    url: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    sources: List[Source] = Field(default_factory=list, description="The sources of the information")
    answer: str = Field(description="The answer to the question")


llm = ChatAnthropic(model="claude-sonnet-5")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke(
        {"messages": [HumanMessage(content="How is the air quality in Chicago today?")]}
    )
    print(result)


if __name__ == "__main__":
    main()
