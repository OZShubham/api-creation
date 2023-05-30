import requests
from behave import given, when, then

signup_api_url = 'https://signup-api-tkstnehxga-el.a.run.app/api/signup'
response = None

@given('the signup API endpoint is available')
def step_given_signup_api_endpoint_available(context):
    # You can perform any necessary setup or validation here
    pass

@when('I send a POST request to the signup API endpoint with valid user data')
def step_when_send_post_request_valid_user_data(context):
    user_data = {
        'name': 'John Doe',
        'email': 'johndoe@example.com',
        'user_role': 'Scrum Master',
        'password': 'password123',
        'user_id': 'johndoe@example.com'
    }
    global response
    response = requests.post(signup_api_url, json=user_data)

@then('the response status code should be 201')
def step_then_response_status_code_201(context):
    assert response.status_code == 201, f"Actual status code: {response.status_code}"

@then('the response should contain a success message')
def step_then_response_contains_success_message(context):
    response_json = response.json()
    assert 'success' in response_json and response_json['success'], "Response does not contain a success message"

@when('I send a POST request to the signup API endpoint with existing user email')
def step_when_send_post_request_existing_user_email(context):
    user_data = {
        'name': 'Shubham Mishra',
        'email': 'shubham@gmail.com',
        'user_role': 'scrum_team_member',
        'password': '12345',
        'user_id': 'shubham@gmail.com'
    }
    global response
    response = requests.post(signup_api_url, json=user_data)

@then('the response status code should be 400')
def step_then_response_status_code_400(context):
    assert response.status_code == 400, f"Actual status code: {response.status_code}"

@then('the response should contain an error message')
def step_then_response_contains_error_message(context):
    response_json = response.json()
    assert 'error' in response_json and response_json['error'], "Response does not contain an error message"
