Feature: Create Poker Board API

Scenario: Successful creation of a poker board
    Given a user with email "rahul@gmail.com"
    When they create a poker board with name "Board 1", team ID "123", and type "Fibonacci Number"
    Then they should receive a success response with status code 201

Scenario: Invalid request method
    When they send a GET request to "/api/create_poker_board"
    Then they should receive a response with status code 405    
