import requests
url = 'https://scrum-team-member-view-noxhrtfvua-el.a.run.app/api/scrum_team_member_view'
data = {
    'user_name' : 'Ankur',
    'story_point' : 12,
    'email' : 'ankur@gmail.com',
    'user_id' : 'ankur@gmail.com',
    'poker_board_id' : '120e3315b2b3930b89345d6caae749f3',
    'jira_id' : 'PEWA_1'
}

headers = {"Content-Type": "application/json" }
response = requests.post(url, json=data)

