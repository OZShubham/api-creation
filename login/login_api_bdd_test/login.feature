Feature: User Login API

  Scenario: Successful Login
    Given a user with email "shubham@gmail.com" and password "12345"
    When I make a POST request to "/api/login" with the following JSON data:
      """
      {
        "email": "shubham@gmail.com",
        "password": "12345"
      }
      """
    Then the response status code should be 200
    And the response should contain the message "User logged in successfully"

  

  Scenario: Incorrect Password
    Given a user with email "shubham@gmail.com" and password "incorrect"
    When I make a POST request to "/api/login" with the following JSON data:
      """
      {
        "email": "shubham@gmail.com",
        "password": "incorrect"
      }
      """
    Then the response status code should be 401
    And the response should contain the error message "Incorrect Password"

  Scenario: User Not Found
    Given a user with email "unknown@gmail.com" and password "unknown"
    When I make a POST request to "/api/login" with the following JSON data:
      """
      {
        "email": "unknown@gmail.com",
        "password": "unknown"
      }
      """
    Then the response status code should be 404
    And the response should contain the error message "User not found"
