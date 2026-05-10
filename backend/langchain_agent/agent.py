from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import AgentType

from langchain_agent.tools import all_tools
from langchain_agent.memory import memory
from langchain_agent.prompts import SYSTEM_PROMPT
import os
from dotenv import load_dotenv

load_dotenv()

llm=ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY"),
)

agent=initialize_agent(
    tools=all_tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    agent_kwargs={
        "system_message": SYSTEM_PROMPT
    }
)
