from IPython.display import Markdown, display
import markdown2
import requests

def ask_api_pretty(question):
    response = requests.post("http://localhost:8000/chat", json={"query": question}, stream= True)
    answer = response.json().get("response")
    html = markdown2.markdown(answer, extras=["fenced-code-blocks", "tables"])
    display(Markdown(answer))

ask_api_pretty("Explain radiusclientlist")

