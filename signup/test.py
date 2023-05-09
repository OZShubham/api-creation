'''import requests
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
print(response.json())'''


import requests
url = 'https://create-jira-tkstnehxga-el.a.run.app/api/create_jira_id'
data = {
   

    'poker_board_id' : '15544fa60c8218588fcbbaf6a245b261',
    'jira_id' :'apitest',
    'jira_description' : 'testing api',
    'jira_title' : 'pe-test'
}

response = requests.post(url, json=data)
print(response.json())
