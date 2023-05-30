

## Overview
This API allows users to fetch the poker boards using a POST request to the `/api/master_board` endpoint. 

## Endpoints

### POST /api/master_board
This endpoint allows users to fetch the poker boards by providing their email

#### Request Body

The request body should be a JSON object with the following fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|

| email | string | Yes | The user's email address |



Example Request Body:
```
{
    'email': 'babu@gmail.com',
}
```

#### Responses

| Status Code | Response Body | Description |
|-------------|---------------|-------------|
| 401 | `{'error': "Create a Poker Board"}` | The user has not created any Created Board |
| 400 | `{'error': 'Invalid request payload'}` | A payload without email  |

## Libraries used

- Flask: A Python web framework for building web applications.
- jsonify: A Flask utility function that converts Python objects to JSON format.
- request: A Flask utility function that provides access to incoming request data.
- Google Cloud Datastore: A fully-managed NoSQL document database service that runs on Google Cloud Platform.