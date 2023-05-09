import requests
url = 'https://poker-service-tkstnehxga-el.a.run.app/api/signup'
data = {
    'name': 'shubhamtest',
    'email': 'test@example.com',
    'user_id': 'test@example.com',
    'user_role': 'team member',
    'password': '123',
    'confirm_password': '123'
}

response = requests.post(url, json=data)
print(response.json())


