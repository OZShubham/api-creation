import requests

# Define the API endpoint URL
url = 'https://member-board-api-tkstnehxga-el.a.run.app/api/member_board'

# Define the request payload
payload = {'email': 'shubham@gmail.com'}

# Send a POST request to the endpoint
response = requests.post(url, json=payload)

# Print the response
print(response.text)

