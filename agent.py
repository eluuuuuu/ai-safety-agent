from dotenv import load_dotenv
from pathlib import Path
import os
from langchain_openai import AzureChatOpenAI
from safety import check_content

# Load .env from project root
dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

# Optional: confirm keys are loaded
print("OPENAI KEY:", os.getenv("AZURE_OPENAI_API_KEY"))
print("ENDPOINT:", os.getenv("AZURE_OPENAI_ENDPOINT"))

# Create LLM
llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    deployment_name="gpt-4.1",
    api_version="2024-02-15-preview",
    temperature=0
)

def run_agent(user_input: str) -> str:
    if not check_content(user_input):
        return "❌ Input failed safety check."

    response = llm.invoke(user_input)
    text = response.content

    if not check_content(text):
        return "❌ Output failed safety check."

    return text

if __name__ == "__main__":
    print("AI Safety Agent running. Type 'exit' to quit.")
    while True:
        msg = input("You: ")
        if msg.lower() == "exit":
            break
        print("Agent:", run_agent(msg))