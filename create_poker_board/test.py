import requests
url = 'https://create-poker-board-noxhrtfvua-el.a.run.app/api/create_poker_board'
data = {
    'email': 'test@example.com',
    'poker_board_name' : 'Sixth',
    'team_id' : '121',
    'poker_board_type' : ''
}

response = requests.post(url, json=data)
print(response.json())
