

## Overview
This API allows users to sign up by sending a POST request to the `/api/signup` endpoint. User data is stored in Google Cloud Datastore, and passwords are hashed using the bcrypt library.

## Endpoints

### POST /api/signup
This endpoint allows users to create an account by providing their name, email, user role, password.

#### Request Body

The request body should be a JSON object with the following fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | Yes | The user's name |
| email | string | Yes | The user's email address |
| user_role | string | Yes | The user's role, e.g., "admin", "user", etc. |
| password | string | Yes | The user's password |


Example Request Body:
```
{
    'name': 'shubhamtest',
    'email': 'test@example.com',
    'user_id': 'test@example.com',
    'user_role': 'team member',
    'password': '123',
    
}
```

#### Responses

| Status Code | Response Body | Description |
|-------------|---------------|-------------|
| 201 | `{"success": "Account Created Successfully!"}` | Account was created successfully |
| 400 | `{"error": "User with this email already exists"}` | A user with this email address already exists |

## Libraries used

- Flask: A Python web framework for building web applications.
- jsonify: A Flask utility function that converts Python objects to JSON format.
- request: A Flask utility function that provides access to incoming request data.
- bcrypt: A password-hashing library that uses the bcrypt algorithm to hash passwords.
- Google Cloud Datastore: A fully-managed NoSQL document database service that runs on Google Cloud Platform.