import requests

url = 'https://scrum-master-choose-jira-noxhrtfvua-el.a.run.app/choose_jira_id'
params = {
    'poker_board_id': '53604617f13c35adf1097a295dc91ad4'
}

response = requests.get(url, params=params)
print(response.json())
