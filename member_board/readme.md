# API Documentation - Member Board

This API fetches poker boards and user name  based on their email.

## Endpoint

```
POST /api/member_board
```

## Request

The API accepts a JSON payload in the request body with the following parameter:

| Parameter | Type   | Description            |
|-----------|--------|------------------------|
| email     | string | Email of the user      |

Example Request:

```http
POST /api/member_board HTTP/1.1
Host: localhost:5000
Content-Type: application/json

{
  "email": "example@example.com"
}
```

## Response

The API responds with JSON data containing the user's boards and name.

- If the user is found, the API will respond with HTTP status code 200 (OK) and the following JSON structure:

```json
{
  "boards": ["board1", "board2", "board3"],
  "name": "John Doe"
}
```

- If the user is not found, the API will respond with HTTP status code 404 (Not Found) and the following JSON structure:

```json
{
  "error": "User not found"
}
```

Example Response (User found):

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "boards": ["board1", "board2", "board3"],
  "name": "John Doe"
}
```

Example Response (User not found):

```http
HTTP/1.1 404 Not Found
Content-Type: application/json

{
  "error": "User not found"
}
```


