import requests

def handle_message(message, history=None):
	API_URL = "http://127.0.0.1:3000/api/v1/prediction/424fd725-0e11-4ff0-a3a4-8b3a6548fa03"

	def query(payload):
		response = requests.post(API_URL, json=payload)
		return response.json()
		
	output = query({
		"question": message
	})
	
	return output['text']