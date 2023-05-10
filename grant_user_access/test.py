import requests

# Set the URL of the Cloud Run service
url = 'https://grant-user-access-tkstnehxga-el.a.run.app/api/grant_user_access'

# Set the JSON data to send in the request
data = {
    'email': 'babu@gmail.com',
    'poker_board_id': '15544fa60c8218588fcbbaf6a245b261',
    'user_ids': ['test@example.com']
}

# Send the POST request with the JSON payload and headers
response = requests.post(url, json=data)

# Check the response status code and content
if response.status_code == 200:
    print('Access granted successfully!')
else:
    print(f'Error granting access: {response.status_code} {response.json()}')




