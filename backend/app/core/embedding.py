import requests

def embedding(texts):
    url = "http://127.0.0.1:1234/v1/embeddings"

    payload = {
        "model": "text-embedding-nomic-embed-text-v1.5",
        "input": texts
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    result = response.json()

    return [item["embedding"] for item in result["data"]]