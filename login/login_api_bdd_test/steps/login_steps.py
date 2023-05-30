import requests
from behave import given, when, then

api_url = 'https://login-tkstnehxga-el.a.run.app'
response = None

@given('a user with email "{email}" and password "{password}"')
def step_given_user_with_email_and_password(context, email, password):
    context.email = email
    context.password = password

@when('I make a POST request to "/api/login" with the following JSON data')
def step_when_make_post_request(context):
    data = {
        "email": context.email,
        "password": context.password
    }
    global response
    response = requests.post(f"{api_url}/api/login", json=data)



@then('the response status code should be {status_code}')
def step_then_response_status_code(context, status_code):
    assert response.status_code == int(status_code), f"Actual status code: {response.status_code}"

@then('the response should contain the message "{message}"')
def step_then_response_contains_message(context, message):
    response_json = response.json()
    assert 'message' in response_json and response_json['message'] == message, "Response does not contain the expected message"

@then('the response should contain the error message "{error_message}"')
def step_then_response_contains_error_message(context, error_message):
    response_json = response.json()
    assert 'error' in response_json and response_json['error'] == error_message, "Response does not contain the expected error message"
