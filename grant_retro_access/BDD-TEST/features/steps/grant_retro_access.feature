Feature: Grant Retro Access API

  Scenario: Grant user access to a retro board
    Given the API endpoint is available
    When a POST request is made to "/api/grant_retro_access" with valid data
    
    | email           | retro_board_id                   | user_ids |
    | ankur@gmail.com | 1182b2d344ffac2e4302e118204bb799 | test_sign_up@test.com  |
    | ankur@gmail.com | 5a82ed9972501fb1fd10ad381bc3563d | test_sign_up@gmail.com  |
    
    Then the response should contain the message "Access granted successfully"