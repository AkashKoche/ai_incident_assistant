import subprocess
from langchain.tools import tool

@tool
def get_pods(namespace: str = "default") -> str:

    result = subprocess.run(
            ["kubectl", "get", "pods", "-n", namespace],
            capture_output=True, text=True
    )
    return result.stdout if result.returncode == 0 else result.stderr

@tool
def get_logs(pod_name: str, namespace: str = "default", tail: int = 50) -> str:

    result = subprocess.run(
            ["kubectl", "logs", pod_name, "-n", namespace, f"--tail={tail}"],
            capture_output=True, text=True
    )
    return result.stdout if result.returncode == 0 else result.stderr

@tool
def describe_pod(pod_name: str, namespace: std = "default") -> str:

    result = subprocess.run(
            ["kubectl", "describe", "pod", pod_name, "-n", namespace],
            capture_output=True, text=True
    )

    return result.stdout if result.returncode == 0 else result.stderr
