

# Reset Password API

This API allows you to reset the password for a user by providing their email and a new password.

## Endpoint

```
/api/reset_password
```

## Method

- GET, POST

## Request Parameters

The API expects a JSON payload with the following parameters:

- `email` (string, required): The email address of the user whose password needs to be reset.
- `new_password` (string, required): The new password for the user.

## Request Example

```json
{
  "email": "user@example.com",
  "new_password": "newpassword123"
}
```

## Response

- Success (HTTP 200 OK):

  ```json
  {
    "success": "Password reset successfully!"
  }
  ```

- Error (HTTP 400 Bad Request):

  ```json
  "Email and new password are required"
  ```

## Examples

### Request

```http
POST /api/reset_password
Content-Type: application/json

{
  "email": "user@example.com",
  "new_password": "newpassword123"
}
```

### Response

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "success": "Password reset successfully!"
}
```

## Notes

- This API uses the Flask web framework and Google Cloud Datastore for data storage.
- The API verifies if the provided email exists in the database before resetting the password.
- If the email is found, the user's password is updated with the new password in the database.

