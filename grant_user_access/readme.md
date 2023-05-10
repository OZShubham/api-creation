 # Grant User Access API

This is a Python Flask application that provides a REST API for granting access to a PokerBoard to selected users.

## Requirements

- `Python`
- `Flask`
- `google-cloud-datastore`

# API Endpoints
## Grant User Access

This API endpoint (/api/grant_user_access) allows a Scrum Master user to grant access to a PokerBoard to selected users.

- `POST /api/grant_user_access`

Grants access to a poker board for one or more users.

## Request
| Field | Type | Description |
|-------|------|-------------| 
| email | String | The email address of the Scrum Master |
| poker_board_id	| string |The ID of the Poker Board to grant access |
| user_ids | list | A list of user IDs to grant access to the board |

## Example Usage

```
{
    "email": "scrummaster@example.com",
    "poker_board_id": "12345678",
    "user_ids": ["user1", "user2", "user3"]
}

```

## Response

- 200 OK: Successfully granted access
- 401 Unauthorized: User does not have Scrum Master role
- 404 Not Found: Poker Board does not exist

```

{
  "success": true
}

```

- `POST /api/create_poker_board`

Creates a new poker board.

## Request Body

```
{
  "email": "user@example.com",
  "poker_board_id": "poker_board_id",
  "poker_board_name": "poker_board_name",
  "poker_board_type": "poker_board_type"
}

```
## Response

- 200: Successfully created poker board
- 404 Bad Request: Missing required fields in request body

```
Copy code
{
  "success": "Poker Board Created Successfully!"
}

```
## Running the API

To start the API, run the following command in your terminal:

```
python app.py

```





