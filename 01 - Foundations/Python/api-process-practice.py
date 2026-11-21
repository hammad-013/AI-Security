import requests

res = requests.get("https://prod-main-api-704464-00tre1p1erm.compute.instacloud-edge.com/api/v1/public/meals/meal/random")
body = res.json()

print("Status Code: ", body["statusCode"])
print("Name: ", body["data"]["strMeal"])
print("instructions: ", body["data"]["strInstructions"])
