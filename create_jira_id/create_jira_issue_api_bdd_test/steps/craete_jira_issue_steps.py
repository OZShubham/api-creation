import requests
from behave import given, when, then

base_url = 'https://create-jira-tkstnehxga-el.a.run.app'  # Replace with the actual Cloud Run URL

@given('I have a valid Poker Board ID')
def step_given_valid_poker_board_id(context):
    context.poker_board_id = '046952ea1fc2e24af514ecf623756fbe'

@when('I send a POST request to "{endpoint}" with valid data')
def step_when_send_post_request(context, endpoint):
    url = f'{base_url}{endpoint}'
    data = {
        'poker_board_id': context.poker_board_id,
        'jira_id': 'valid-jira-id',
        'jira_description': 'valid-jira-description',
        'jira_title': 'valid-jira-title'
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, json=data, headers=headers)
    context.response = response

@then('I receive a successful response')
def step_then_receive_successful_response(context):
    assert context.response.status_code == 200
    assert context.response.json().get('success') == True

@when('I send a POST request to "{endpoint}" with missing fields')
def step_when_send_post_request_missing_fields(context, endpoint):
    url = f'{base_url}{endpoint}'
    data = {
        'poker_board_id': context.poker_board_id,
        'jira_id': ' ',
        'jira_description': ' ',

    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, json=data, headers=headers)
    context.response = response

@then('I receive an error response')
def step_then_receive_error_response(context):
    assert context.response.status_code == 400
    assert context.response.json().get('error') == True



