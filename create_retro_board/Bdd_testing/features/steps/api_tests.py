import behave
import requests

# Set the base URL of your Flask application
BASE_URL = 'https://create-retro-board-noxhrtfvua-el.a.run.app'

@behave.given('a user with email "{email}"')
def step_given_user_with_email(context, email):
    context.email = email

@behave.when('they create retro board with the following details')
def step_when_create_retro_board(context):
    for row in context.table:
        data = {
        'email': context.email,
        'retro_board_name': row['board_name'],
        'team_id': row['team_id'],
        'poker_board_id': row['board_id']
        }
        response = requests.post(BASE_URL + '/api/create_retro_board', json=data)
        context.response = response

@behave.then('they should receive a success response with status code {status_code}')
def step_then_receive_success_response(context, status_code):
    assert context.response.status_code == int(status_code)
    response_json = context.response.json()
    print("Response JSON:", response_json)  # Print the actual response JSON
    assert response_json.get('success') == 'Retro Board Created Successfully!'

@behave.when('they send a GET request to "{url}"')
def step_when_send_get_request(context, url):
    response = requests.get(BASE_URL + url)
    context.response = response

@behave.then('they should receive a response with status code {status_code}')
def step_then_receive_response(context, status_code):
    assert context.response.status_code == int(status_code)
