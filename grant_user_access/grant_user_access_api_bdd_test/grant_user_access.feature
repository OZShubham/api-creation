

Feature: Grant User Access API

  Scenario: Grant user access to a poker board
    Given the API endpoint is available
    When a POST request is made to "/api/grant_user_access" with valid data
    
    | email          | poker_board_id                   | user_id_list |
    | babu@gmail.com | dd28636345a0f55b454fda8f1e7f3791 | n@gmail.com  |
    | babu@gmail.com | ff28636345a0f55b454fda8f1e7f3791 | rahul@gmail.com  |
    
    Then the response should contain the message "Access granted successfully"
   