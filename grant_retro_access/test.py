import requests

# Set the URL of the Flask application hosting the API
url = 'https://retro-access-zlf25kyp3a-el.a.run.app/api/grant_retro_access'  # Update with your actual URL

# Set the JSON data to send in the request
data = {
    'email': 'ankur@gmail.com',
    'retro_board_id': '1182b2d344ffac2e4302e118204bb799',
    'user_ids': ['test_login@gmail.com']
}

# Send the POST request with the JSON payload and headers
response = requests.post(url, json=data)

# Check the response status code and content
if response.status_code == 200:
    print('Access granted successfully!')
else:
    print(f'Error granting access: {response.status_code} {response.json()}')
