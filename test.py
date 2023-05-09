import requests
url = 'https://login-zlf25kyp3a-el.a.run.app/api/login'
data = {
    
    'email': 'lokesh@gmail.com',
    'password': '123'
   
}

response = requests.post(url, json=data)
print(response.json())
