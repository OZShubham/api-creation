from behave import *
import requests

# Set the base URL of your Flask application
BASE_URL = 'https://scrum-team-retro-view-noxhrtfvua-el.a.run.app'


@given('a retro board with ID "{retro_board_id}"')
def step_given_retro_board_id(context, retro_board_id):
    context.retro_board_id = retro_board_id


@when('a team member with email "{email}" sends their data to the retro board')
def step_when_send_team_member_data(context, email):
    data = dict(context.table[0].as_dict())
    data['retro_board_id'] = context.retro_board_id
    data['email'] = email
    context.response = requests.post(BASE_URL + '/api/scrum_team_retro_view', json=data)

@then('the API should return a success response')
def step_then_api_should_return_success_response(context):
    assert context.response.status_code == 201
    assert context.response.json() == {'success': 'Team member data sent successfully!'}


@when('a team member with email "{email}" sends their data to the non-existent retro board')
def step_when_send_team_member_data_with_get(context, email):
    data = dict(context.table[0].as_dict())
    data['retro_board_id'] = context.retro_board_id
    data['email'] = email
    response = requests.post(BASE_URL + '/api/scrum_team_retro_view', json=data)
    context.response = response

@then('the API should return a 404 error')
def step_then_api_should_return_404_error(context):
    print(context.response.status_code)
    assert context.response.status_code == 404
    response_json = context.response.json()
    assert context.response.json() == {'error': 'Retro Board with this retro_board_id not found'}


@when('a team member with email "{email}" sends their data to the retro board using the GET method')
def step_when_send_team_member_data_with_get(context, email):
    response = requests.get(BASE_URL + '/api/scrum_team_retro_view')
    context.response = response

@then('the API should return a 405 error')
def step_then_api_should_return_405_error(context):

    assert context.response.status_code == 405
    assert context.response.json() == {'error': 'Method not allowed'}
