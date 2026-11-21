import httpx as h
import json

response = h.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41")
print(response.status_code)
print(response.headers["content-type"])
print(json.loads(response.content.decode("utf-8")))
