import requests

# Define the API endpoint URL
url = 'https://retro-member-zlf25kyp3a-el.a.run.app/api/choose_retro_board_member'

# Define the request payload with email and poker_board_id
payload = {'email': 'gautam@gmail.com'}

# Send a POST request to the endpoint
response = requests.post(url, json=payload)

# Print the response
print(response.text)
