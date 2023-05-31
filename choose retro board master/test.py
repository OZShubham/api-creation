import requests

# Define the API endpoint URL
url = 'https://retro-master-zlf25kyp3a-el.a.run.app/api/choose_retro_board_master'

# Define the request payload with email and poker_board_id
payload = {'email': 'ankur@gmail.com', 'poker_board_id': '031413e74f728f906955a6a3ce8d5424'}

# Send a POST request to the endpoint
response = requests.post(url, json=payload)

# Print the response
print(response.text)
