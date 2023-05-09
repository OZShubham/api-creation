## Overview
This API allows users to create jira title along with id and jira description by sending a request to the `/api/create_jira_id` endpoint. 


## Endpoint
- `POST /api/create_jira_id`

## Request

| Field | Type | Required |
|-------|------|----------|
| poker_board_id | string | Yes | 
| jira_id | string | Yes |
| jira_description | string | Yes |
| jira_title | string | Yes | 
| confirm_password | string | Yes |

- `poker_board_id` (required): a string representing the ID of the PokerBoard to which the Jira story is being added.
- `jira_id` (required): a string representing the ID of the Jira story.
- `jira_description` (required): a string representing the description of the Jira story.
- `jira_title` (required): a string representing the title of the Jira story.

## Response
- Success: If the Jira story is successfully added to the PokerBoard, the API will return a JSON response with a `200 OK` status code and the following payload:
```
{
    "success": true
}
```
- Error: If the request payload is invalid, or if the specified PokerBoard does not exist, the API will return a JSON response with a `400 Bad Request` or `404 Not Found` status code and an error message payload in the following format:
```
{
    "error": "string"
}
```

## Examples
### Request
```
POST /api/create_jira_id
Content-Type: application/json

{
    "poker_board_id": "123",
    "jira_id": "ABC-123",
    "jira_description": "As a user, I want to be able to login to the application, so that I can access my account.",
    "jira_title": "User login feature"
}
```

### Response
```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "success": true
}
```