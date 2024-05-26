import requests

API_URL = "https://api-inference.huggingface.co/models/google/gemma-7b-it"
headers = {"Authorization": "ｘｘｘｘｘｘＰｕｔ　Ｙｏｕｒ　ＡＰＩ　Ｈｅｒｅ　ｘｘｘｘｘｘ"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Can you please let us know more details about your ",
})

print (output)
