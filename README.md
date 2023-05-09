Sure, here's a more detailed documentation of the Flask API for user authentication:

## API Documentation

### Login Endpoint

This endpoint is used to authenticate a user by their email and password. It can be accessed through a POST request to `/api/login`.

#### Request

**HTTP Method:** POST

**Request URL:** `/api/login`

**Request Body:**

The request body should be a JSON object with the following fields:

- `email` (required): A string representing the user's email address
- `password` (required): A string representing the user's password

Example Request Body:

```json
{
    "email": "johndoe@example.com",
    "password": "password123"
}
```

#### Response

##### Success Response

If the email and password are valid, the endpoint returns a JSON response with a `201 Created` status code and the following fields:

- `success`: A boolean value indicating whether the authentication was successful or not
- `message`: A string value indicating the result of the authentication

Example Success Response:

```json
{
    "success": true,
    "message": "Sign-in successful"
}
```

##### Error Responses

If the email or password are invalid, the endpoint redirects to the `/login` page and displays an error message. The response will have a `302 Found` status code.

Additionally, if there is an error during the authentication process, the endpoint returns a JSON response with a `203 Non-Authoritative Information` status code and the following fields:

- `success`: A boolean value indicating whether the authentication was successful or not
- `message`: A string value indicating the error message

Example Error Response:

```json
{
    "success": false,
    "message": "Login unsuccessful"
}
```

#### Request Limitations

This endpoint only accepts POST requests. Any other HTTP method will result in a `405 Method Not Allowed` status code.

## Dependencies

This Flask API uses the following dependencies:

- Flask (version 1.1.2)
- bcrypt (version 3.2.0)
- google-cloud-datastore (version 2.0.2)