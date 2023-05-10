import requests

url = 'https://reset-password-zlf25kyp3a-el.a.run.app/api/reset_password'
data = {
    'email': 'rahul123sharma@gmail.com',
    'new_password': '125'
}

response = requests.post(url, json=data)
print(response.json())

