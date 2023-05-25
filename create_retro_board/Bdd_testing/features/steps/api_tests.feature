Feature: Create Retro Board API

Scenario: Successful creation of a retro board
    Given a user with email "rahul@gmail.com"
    When they create a retro board with name "retro-5", team ID "123", and id "53604617f13c35adf1097a295dc91ad5"
    Then they should receive a success response with status code 201

Scenario: Invalid request method
    When they send a GET request to "/api/create_retro_board"
    Then they should receive a response with status code 405    
