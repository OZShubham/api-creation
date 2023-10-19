Feature: Create Poker Board API

Scenario: Successful creation of a poker board
    Given a user with email "rahul@gmail.com"
    When they create poker board with the following details
        | name    | team ID | type              |
        | Board 3 | 123     | Fibonacci Number  |
        | Board 4 | 123     | T-shirt Sizing  |
    Then they should receive a success response with status code 201

Scenario: Invalid request method
    When they send a GET request to "/api/create_poker_board"
    Then they should receive a response with status code 405    
