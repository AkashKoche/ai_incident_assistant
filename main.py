from langchain.agents import create_agent
from langchain_ollama import ChatOllama

from tools import get_pods, get_logs, describe_pod

# LLM
llm = ChatOllama(
    model="llama3.2:3b", 
    temperature=0
)

tools = [get_pods, get_logs, describe_pod]

# Create agent (NEW WAY)
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
You are a Kubernetes SRE assistant.
Debug issues using tools.
Give clear root cause and fix.
"""
)

# Run
response = agent.invoke({
    "messages": [{"role": "user", "content": "Why is my payment pod failing?"}]
})

print(response)
