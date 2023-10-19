import requests
url = 'https://scrum-team-retro-view-noxhrtfvua-el.a.run.app/api/scrum_team_retro_view'
data = {
    'retro_board_id' : '05dbff9691088efe5e2993e812e47b67',
    'email': 'shubham@gmail.com',
    'what_went_well' : 'Hi, this is shubham',
    'what_went_wrong' : 'Nothing!',
    'what_can_be_improved' : 'Everything'
}

response = requests.post(url, json=data)
print(response.json())