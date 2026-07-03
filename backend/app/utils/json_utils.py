import json
import re


def clean_json_response(response: str) -> dict:
    """
    Clean and parse JSON returned by the LLM.
    """

    response = response.strip()

    # Remove markdown fences
    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    # Extract JSON object
    start = response.find("{")
    end = response.rfind("}")

    if start == -1 or end == -1:
        raise ValueError("No valid JSON found in LLM response.")

    json_string = response[start:end + 1]

    # Remove trailing commas before ] or }
    json_string = re.sub(r",\s*([\]}])", r"\1", json_string)

    try:
        return json.loads(json_string)

    except json.JSONDecodeError as e:
        print("=" * 80)
        print("INVALID JSON FROM LLM")
        print(json_string)
        print("=" * 80)
        raise e