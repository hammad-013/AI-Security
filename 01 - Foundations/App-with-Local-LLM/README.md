# Python Ollama LLM Client

A lightweight command-line Python client for chatting with a local LLM.

## Features
- Interactive multi-turn terminal loop (`exit` or `quit` to stop)
- Input validation to ignore empty/whitespace submissions
- Externalized configuration via `.env`
- Graceful handling of network timeouts and HTTP/API errors

## Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com/) installed and pulled a model like `qwen2.5:3b`

## Setup

1. **Install dependencies:**

   ```bash
   pip install requests python-dotenv`
   ```
2. Create a .env file in the project root:

	```bash
	OLLAMA_MODEL=llama3.2
	OLLAMA_BASE_URL=http://localhost:11434/api
	```
	(Adjust OLLAMA_BASE_URL to http://localhost:11434 if your script posts to /api/chat.)
	
## Usage
Run the client:

	```bash
	python main.py
	```
Enter your question at the prompt (e.g., Explain network segmentation.), or type exit / quit to close the program.
