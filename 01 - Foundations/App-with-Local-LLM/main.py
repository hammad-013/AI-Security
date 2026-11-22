from fastapi import FastAPI, Depends, HTTPException, Header
import ollama
import os
from dotenv import load_dotenv

load_dotenv()

API_KEYS = {os.getenv("API_KEY")}

app = FastAPI()

def verify_api_key(api_key: str = Header(None)):
	if api_key not in API_KEYS:
		raise HTTPException(status_code=401, detail="Invalid API Key")
	return api_key

@app.post("/generate")
def generate(prompt: str, api_key: str = Depends(verify_api_key)):
	response = ollama.chat(model="qwen2.5:3b", messages=[{"role": "user", "content": prompt}])
	return {"response": response["message"]["content"]}
