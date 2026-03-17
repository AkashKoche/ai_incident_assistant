from langchain.agents import initialize_agent, AgentType
from langchain_community.llms import Ollama
from tools import get_pods, get_logs, describe_pod

llm = Ollama(model="llama3.2:3b", temprature=0)

tools = [get_pods, get_logs, describe_pod]

agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
)

if __name__ == "__main__":
    query = "What's Wrong woth my payment service pod in the default namespace?"
    response = agent.run(query)
    print("\n=== Final Answer")
    print(response)
