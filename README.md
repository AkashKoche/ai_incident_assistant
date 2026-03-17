# AI Setup
    ollama pull llama3.2:3b   # Lightweight and fast

# Python Environment
    mkdir incident-assistant
    cd incident-assistant
    python -m venv venv
    source venv/bin/activate
    pip install langchain langchain-community ollama

# Apply Crashloop Pod

    kubectl apply -f crash.yaml

# Run Assistant

    python main.py
