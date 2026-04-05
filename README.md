# AI Safety Agent

An AI agent that ensures safe interaction with AI models using Azure OpenAI and Azure Content Safety.

## Features

- **Content Safety Checks**: Automatically filters unsafe input/output using Azure Content Safety.
- **Azure OpenAI Integration**: Uses GPT-4.1 via Azure OpenAI for generating responses.
- **Secure Environment**: Sensitive keys and endpoints are loaded from `.env` and never committed to the repository.
- **Tested and Ready for CI/CD**: Integrated with Azure DevOps pipeline for automated testing.

## Requirements

- Python 3.11+
- Azure OpenAI and Azure Content Safety API keys
- `pip` packages listed in `requirements.txt`

## Installation

1. Clone the repository:

```bash
git clone https://github.com/eluuuuuu/ai-safety-agent.git
cd ai-safety-agent
