import os
import requests
from dotenv import load_dotenv

load_dotenv()

AZURE_CS_ENDPOINT = os.getenv("AZURE_CONTENT_SAFETY_ENDPOINT")
AZURE_CS_KEY = os.getenv("AZURE_CONTENT_SAFETY_KEY")

def check_content(text: str) -> bool:
    url = f"{AZURE_CS_ENDPOINT}/contentsafety/text:analyze?api-version=2023-10-01"

    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_CS_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "text": text
    }

    response = requests.post(url, headers=headers, json=body)
    result = response.json()

    for category in result.get("categoriesAnalysis", []):
        if category["severity"] > 2:
            return False

    return True