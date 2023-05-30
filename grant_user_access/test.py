import requests

url = 'https://grant-user-access-tkstnehxga-el.a.run.app/api/grant_user_access'
payload = {
    'email': 'babu@gmail.com',
    'poker_board_id': 'dd28636345a0f55b454fda8f1e7f3791',
    'user_id_list': ['retro@gmail.com']
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    print('Access granted successfully')
    print(response.json())
else:
    print('Error:', response.status_code)
    print(response.json())
