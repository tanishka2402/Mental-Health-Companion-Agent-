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

print("AI Agent is ready. Type your questions below. Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    inputs = {"messages": [{"role": "user", "content": user_input}]}
    print("Agent: ", end="")
    for chunk in agent.stream(inputs, stream_mode="updates"):
        if 'agent' in chunk:
            message = chunk['agent']['messages'][-1]
            print(message.content, end="")
    print("\n")
