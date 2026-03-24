Local Incident Response Assistant is a specialized SRE agent designed to automate Kubernetes troubleshooting. By combining the reasoning capabilities of Llama 3.2 with direct cluster access, it can identify, describe, and log-analyze failing pods to provide a definitive root cause in seconds.


⚙️ Core Architecture

The system is built on a "Reasoning and Action" loop:

    The Brain: A local ChatOllama instance running llama3.2:3b with a zero-temperature setting for consistent, factual debugging.

    The Hands: A custom set of LangChain tools that wrap kubectl commands to interact with the live cluster.

    The Agent: A LangChain agent that determines which tool to call based on the user's natural language query.


🛠️ Integrated Tools

The agent has access to the following capabilities via tools.py:
| Tool | Function | kubectl Equivalent |
| :--- | :--- | :--- |
| get_pods | Lists all pods in a namespace to check status. | kubectl get pods |
| get_logs | Fetches the last 50 lines of container logs. | kubectl logs --tail=50 |
| describe_pod | Provides deep metadata and cluster events. | kubectl describe pod |


🚀 Quick Start
1. Simulate a Failure

Deploy the included crash.yaml to create a pod that is hardcoded to fail after five seconds:


    kubectl apply -f crash.yaml

2. Configure the Environment

Ensure Ollama is running locally and you have the required Python packages:


    pip install langchain langchain_ollama

3. Run the Assistant

Execute main.py to start the diagnostic session. The agent will automatically detect that the payment-service pod is crashing because of the exit 1 command in its specification.


📝 Project Files

    crash.yaml: A Kubernetes manifest for a payment-service pod using a busybox image that triggers a crash loop.

    tools.py: Python functions decorated with @tool that use subprocess to execute cluster commands safely.

    main.py: The entry point that initializes the LLM, binds the tools, and invokes the agent with a user prompt.
