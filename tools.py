import subprocess
from langchain.tools import tool

@tool
def get_pods(namespace: str = "default") -> str:
    """Lists all pods in a given Kubernetes namespace. 
    Useful for seeing the status of pods (Running, Pending, Error, etc.)."""
    result = subprocess.run(
            ["kubectl", "get", "pods", "-n", namespace],
            capture_output=True, text=True
    )
    return result.stdout if result.returncode == 0 else result.stderr

@tool
def get_logs(pod_name: str, namespace: str = "default", tail: int = 50) -> str:
    """Fetches the last N lines of logs from a specific pod. 
    Use this to see error traces or application output."""
    result = subprocess.run(
            ["kubectl", "logs", pod_name, "-n", namespace, f"--tail={tail}"],
            capture_output=True, text=True
    )
    return result.stdout if result.returncode == 0 else result.stderr

@tool
def describe_pod(pod_name: str, namespace: str = "default") -> str:
    """Provides detailed information about a specific pod, including events, 
    resource limits, and container status. Use this if a pod is failing to start."""
    result = subprocess.run(
            ["kubectl", "describe", "pod", pod_name, "-n", namespace],
            capture_output=True, text=True
    )
    return result.stdout if result.returncode == 0 else result.stderr
