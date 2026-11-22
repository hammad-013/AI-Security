import os
import requests as rq
from dotenv import load_dotenv

load_dotenv()
MODEL = os.getenv("OLLAMA_MODEL")
URL = os.getenv("OLLAMA_BASE_URL")

def verify_env():
	if MODEL == None or URL == None:
		print("\nModel or URL is not set!\n")
		return False
	return True 

def ask_ollama(prompt: str):
	try:
		data = {"model": MODEL, "messages": [{"role": "user", "content": prompt}], "stream": False}
		response = rq.post(f"{URL.rstrip("/")}/chat", json=data, timeout=60)
		response.raise_for_status()
		return response.json()["message"]["content"]
	except rq.RequestException as e:
		return f"Error Occured: {e}"

def chat_loop():
	while True:
		prompt = input("What do you want to ask?\n").strip()
		if not prompt:
			print("\nEmpty input!!!\n")
		elif prompt.lower() == "exit" or prompt.lower() == "quit":
			print("\nExiting...\n")
			break
		else:
			print(f"\nSending to {MODEL}: {prompt}\n")
			print("Response: ", ask_ollama(prompt))

def main():
	if verify_env() == True:
		chat_loop()

if __name__ == "__main__":
	main()
