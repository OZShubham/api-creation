import requests

# Define the API endpoint URL
url = 'https://master-board-api-tkstnehxga-el.a.run.app//api/master_board'

# Define the request payload
payload = {'email': 'babu@gmail.com'}

# Send a POST request to the endpoint
response = requests.post(url, json=payload)

# Print the response
print(response.text)

