Feature: User Signup API

Scenario: Successful user signup
   Given the signup API endpoint is available
   When I send a POST request to the signup API endpoint with valid user data
   Then the response status code should be 201
   And the response should contain a success message

Scenario: User signup with existing email
   Given the signup API endpoint is available
   When I send a POST request to the signup API endpoint with existing user email
   Then the response status code should be 400
   And the response should contain an error message
