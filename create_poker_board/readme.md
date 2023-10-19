# Flask API Documentation

This Flask API provides functionality for creating a Poker Board using a POST request to the `/api/create_poker_board` endpoint.

## API Endpoint

The API endpoint for creating a Poker Board is:

```
/api/create_poker_board
```

## Request Method

This API endpoint accepts GET and POST requests. 

## Request Parameters

The following parameters are required to create a Poker Board:

| Parameter | Description |
| --- | --- |
| email | The email address of the user creating the Poker Board |
| poker_board_name | The name of the Poker Board |
| team_id | The ID of the team associated with the Poker Board |
| poker_board_type | The type of the Poker Board |

## Request Body

The request body must be a JSON object that contains the required parameters. The keys of the JSON object must match the parameter names described above. 

## Response

The API will return a JSON object with the following keys:

| Key | Description |
| --- | --- |
| success | A success message if the Poker Board was created successfully |
| error | An error message if the request was not successful |

## Response Codes

The following HTTP response codes are returned by the API:

| Code | Description |
| --- | --- |
| 201 | The request was successful and a new Poker Board was created |
| 400 | The request was malformed and did not contain all required parameters |
| 405 | The HTTP request method was not allowed for this endpoint |

## Examples

### Example Request

```
POST /api/create_poker_board HTTP/1.1
Host: example.com
Content-Type: application/json
Content-Length: 96

{
    "email": "jane@example.com",
    "poker_board_name": "Sprint 1 Planning",
    "team_id": "1234",
    "poker_board_type": "planning"
}
```

### Example Response

```
HTTP/1.1 201 Created
Content-Type: application/json

{
    "success": "Poker Board Created Successfully!"
}
```