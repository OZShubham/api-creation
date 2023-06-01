Feature: Retro Board API

  Scenario: Send team member data to the retro board
    Given a retro board with ID "05dbff9691088efe5e2993e812e47b67"
    When a team member with email "shubham@gmail.com" sends their data to the retro board
      | what_went_well                | what_went_wrong                             | what_can_be_improved                           |
      | We completed all the tasks.   | The communication could have been better.   | We should have more frequent meetings.          |
    Then the API should return a success response

  Scenario: Send team member data to a non-existent retro board
    Given a retro board with ID "05dbff9691088efe5e2993e812e47b66"
    When a team member with email "shubham@gmail.com" sends their data to the non-existent retro board
      | what_went_well                | what_went_wrong                             | what_can_be_improved                           |
      | We had productive discussions | Some tasks were not completed on time.      | Better time management is required.             |
    Then the API should return a 404 error

  Scenario: Send team member data using an invalid HTTP method
    Given a retro board with ID "05dbff9691088efe5e2993e812e47b67"
    When a team member with email "shubham@gmail.com" sends their data to the retro board using the GET method
      | what_went_well                | what_went_wrong                             | what_can_be_improved                           |
      | Good collaboration within the team. | Tasks were not assigned properly.        | Better task allocation and planning is needed. |
    Then the API should return a 405 error
