import json

def clean_json_response(response: str) -> dict:
    """
    Extract JSON from LLM response and convert it to Python dictionary.
    """

    response = response.strip()

    # Find JSON object
    start = response.find("{")
    end = response.rfind("}")

    if start == -1 or end == -1:
        raise ValueError("No valid JSON found in LLM response.")

    json_string = response[start:end + 1]

    return json.loads(json_string)