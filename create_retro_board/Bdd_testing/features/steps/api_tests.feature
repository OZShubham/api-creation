Feature: Create Retro Board API

Scenario: Successful creation of a retro board
    Given a user with email "rahul@gmail.com"
    When they create retro board with the following details
        | board_name    | team_id | board_id              |
        | retro-3       | 123     | 53604617f13c35adf1097a295dc91ad5  |
        | retro-4       | 123     | 53604617f13c35adf1097a295dc91ad5  |
    Then they should receive a success response with status code 201

Scenario: Invalid request method
    When they send a GET request to "/api/create_retro_board"
    Then they should receive a response with status code 405    
