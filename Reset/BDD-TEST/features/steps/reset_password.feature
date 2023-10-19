Feature: Password Reset API

  Scenario: Successful password reset
    Given an existing user with email "gautam@gmail.com" and password "1234"
    When a request is made to reset the password with email "gautam@gmail.com" and new password "123"
    Then the API should respond with a success message

  Scenario: User not found
    Given no existing user with email "gautam2@gmail.com"
    When a request is made to reset the password with email "gautam2@gmail.com" and new password "123"
    Then the API should respond with an error message

  Scenario: Missing email or new password
    Given an existing user with email "gopal@gmail.com" and password "123"
    When a request is made to reset the password without providing an email or new password
    Then the API should respond with a bad request error message
