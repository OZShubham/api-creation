from behave import given, when, then
import requests

API_URL = 'https://reset-pass2-zlf25kyp3a-el.a.run.app/api/reset_password'

@given('an existing user with email "{email}" and password "{password}"')
def create_existing_user(context, email, password):
    # You can write code here to create a test user with the given email and password
    pass

@given('no existing user with email "{email}"')
def create_non_existing_user(context, email):
    # You can write code here to ensure that no user with the given email exists
    pass

@when('a request is made to reset the password with email "{email}" and new password "{new_password}"')
def make_reset_password_request(context, email, new_password):
    data = {
        'email': email,
        'new_password': new_password
    }
    context.response = requests.post(API_URL, json=data)

@when('a request is made to reset the password without providing an email or new password')
def make_reset_password_request_without_credentials(context):
    data = {}
    context.response = requests.post(API_URL, json=data)


@then('the API should respond with a success message')
def check_success_response(context):
    response = context.response
    assert response.status_code == 200
    assert response.json() == {'success': 'Password reset successfully!'}

@then('the API should respond with an error message')
def check_error_response(context):
    response = context.response
    assert response.status_code == 404
    assert response.json() == {'error': 'User not found'}

@then('the API should respond with a bad request error message')
def check_bad_request_response(context):
    response = context.response
    print(f"Response status code: {response.status_code}")
    assert response.status_code == 400
    assert response.json() == {'error': 'Email and new password are required'}
