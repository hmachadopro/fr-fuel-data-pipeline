import requests
import dotenv
import json
import os

dotenv.load_dotenv()

url = os.getenv("API_URL")

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4, ensure_ascii=False))
else:
    print(f"Error: {response.status_code}")