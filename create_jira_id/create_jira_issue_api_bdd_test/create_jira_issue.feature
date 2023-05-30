Feature: Create Jira ID
  As a user
  I want to create a Jira ID
  So that I can add it to a Poker Board

  Scenario: Successfully create a Jira ID
    Given I have a valid Poker Board ID
    When I send a POST request to "/api/create_jira_id" with valid data
    Then I receive a successful response

  Scenario: Missing required fields
    Given I have a valid Poker Board ID
    When I send a POST request to "/api/create_jira_id" with missing fields
    Then I receive an error response
