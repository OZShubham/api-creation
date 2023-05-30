import requests
import json
url = 'https://login-tkstnehxga-el.a.run.app/api/login'
data = {
   

    'email' : 'shubham@gmail.com',
    'password' :'1234',
    
}

response = requests.post(url, json=data)
response_data = response.json()
print(response.json())