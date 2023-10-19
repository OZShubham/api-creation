import requests
from behave import given, when, then

@given('the API endpoint is available')
def step_given_api_endpoint_available(context):
    context.api_url = 'https://retro-zlf25kyp3a-el.a.run.app'

@when('a POST request is made to "{endpoint}" with valid data')
def step_when_post_request_with_valid_data(context, endpoint):
    table = context.table
    for row in table:
        context.payload = {
        'email': row['email'],
        'retro_board_id': row['retro_board_id'],
        'user_ids': [row['user_ids']]
        }
        
        context.response = requests.post(context.api_url + endpoint, json=context.payload)
        print(context.response.content)


@then('the response should contain the message "{message}"')
def step_then_response_contains_message(context, message):
    response_data = context.response.json()
    assert message in response_data.get('message', '')

