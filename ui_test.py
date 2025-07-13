import gradio as gr
import requests

API_URL = "http://localhost:8000/chat"

def chatbot_fn(message, history):
    """
    message: str, latest user message
    history: list of [user, bot] pairs
    """

    # Convert history to a flat list of strings if needed
    # For example: ["Hi", "Hello!", "What is X?", "It is Y."]
    flat_history = []
    for pair in history:
        flat_history.extend(pair)

    # Build payload with history
    payload = {
        "query": message,
        "history": flat_history   # This will be sent even if the API ignores it for now
    }

    # Call your FastAPI server
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        answer = response.json().get("response", "I don't know.")
    except Exception as e:
        answer = f"Error contacting backend: {e}"

    return answer

demo = gr.ChatInterface(
    fn=chatbot_fn,
    title="CyberArk API RAG Chatbot",
    description="Ask anything about CyberArk API documentation. The chatbot answers based on RAG retrieval.",
    theme="default",
)

if __name__ == "__main__":
    demo.launch()
