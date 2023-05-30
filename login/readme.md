Certainly! Here's an example of API documentation for the `/api/login` endpoint using the popular Swagger/OpenAPI style:

## API Documentation

### Login

This API endpoint is used to authenticate a user by providing their email and password.

#### Request

- Method: POST
- Endpoint: `/api/login`
- Content-Type: application/json

##### Request Body Parameters

| Name     | Type   | Description           |
|----------|--------|-----------------------|
| email    | string | The user's email address. |
| password | string | The user's password.      |

Example Request Body:
```json
{
  "email": "example@example.com",
  "password": "password123"
}
```

#### Response

##### Success Response

- Status Code: 200
- Content-Type: application/json

Example Response Body:
```json
{
  "message": "User logged in successfully"
}
```

##### Error Responses

- Status Code: 400
- Content-Type: application/json

Example Response Body:
```json
{
  "error": "Invalid request payload"
}
```

- Status Code: 401
- Content-Type: application/json

Example Response Body:
```json
{
  "error": "Incorrect Password"
}
```

- Status Code: 404
- Content-Type: application/json

Example Response Body:
```json
{
  "error": "User not found"
}
```

Please note that this is a basic example, and you may want to customize the documentation further to include additional details, such as API authentication requirements or response schema definitions.