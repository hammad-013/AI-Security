import asyncio as asio
import httpx as hx
import json

async def get_post(client, id, sem, attempts=3):
	async with sem:
		last_error = None
		for attempt in range(1, attempts + 1):
			try:
				res = await asio.wait_for(client.get(f"https://jsonplaceholder.typicode.com/posts/{id}"), timeout=2)
				print(f"Fetching a request {id}...")
				post = res.json()
				return {"id": post["id"], "title": post["title"]}
			except Exception as e:
				last_error = e
				if attempt == attempts:
					raise RuntimeError(f"post {id} timed out")
				print("attempting again...")
				await asio.sleep(0.2 * attempt)

async def main():
	sem = asio.Semaphore(10)
	async with hx.AsyncClient() as cl:
		responses = await asio.gather(*(get_post(cl, i, sem) for i in range(1, 105)), return_exceptions=True)
	posts, failed = [], 0
	for i in responses:
		if isinstance(i, Exception):
			failed += 1
		else: 
			posts.append(i)
	print(f"{len(posts)} succeeded and {failed} failed")
	with open("posts.json", "w", encoding="utf-8") as f:
		json.dump(posts, f, indent=2)

	print(f"{len(posts)} succeeded and {failed} failed.")

asio.run(main())

