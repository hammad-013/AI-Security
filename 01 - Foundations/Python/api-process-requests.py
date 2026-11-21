import requests as rq
import json

response = rq.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m")
print(response.status_code)
print(response.headers.get("content-type"))
print(json.loads(response.content.decode("utf-8")))
