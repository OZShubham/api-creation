import requests
url = 'https://create-retro-board-noxhrtfvua-el.a.run.app/api/create_retro_board'
data = {
    'email': 'rahul@gmail.com',
    'retro_board_name' : 'retro-5',
    'team_id' : '123',
    'poker_board_id' : '53604617f13c35adf1097a295dc91ad5'
}

response = requests.post(url, json=data)
print(response.json())
