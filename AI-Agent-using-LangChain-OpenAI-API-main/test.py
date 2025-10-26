# import os
# from dotenv import load_dotenv
# load_dotenv()

# from langchain.chat_models import ChatOpenAI
# from langchain.agents import initialize_agent, AgentType, load_tools

# llm = ChatOpenAI(temperature=0, model_name="gpt-4o")  

# tools = load_tools(["serpapi", "llm-math"], llm=llm)   

# agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# print(agent.run("Find the latest research news about 'agentic AI' and summarize in 3 bullets."))


import os
from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent


model = init_chat_model("openai:gpt-4o-mini")


agent = create_react_agent(
    model=model,
    tools=[],
    prompt="You are a helpful assistant."
)


# Ask the user for a question
user_question = input("What question do you want to ask the agent? ")

inputs = {"messages": [{"role": "user", "content": user_question}]}
try:
    for chunk in agent.stream(inputs, stream_mode="updates"):
        print(chunk)
except Exception as e:
    print(f"An error occurred while running the agent: {e}")
    print("Please check your internet connection or API key.")
