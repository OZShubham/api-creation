# Flask API for Scrum Team Voting Application

This is a Flask API for a Scrum Team Voting Application. The purpose of this application is to allow Scrum Team Members to vote on User Stories by assigning Story Points to them. The Story Points are used to estimate the relative size and complexity of each User Story.

# Getting Started

# Endpoints

 `/api/scrum_team_member_view`

   This endpoint is used to allow Scrum Team Members to vote on User Stories.

## Request
- HTTP Method: POST

## Request Body:

| Parameter | Type | Required | Description |
| ------ | ---- | -------- | ----------- |
|user_name | string | yes |	The name of the user who is submitting the estimate. |
|user_id |	string | yes |	The ID of the user who is submitting the estimate. |
| story_point | string | yes | The estimate selected by the user. |
|email | string | yes | The email address of the user who is submitting the estimate. |
|poker_board_id	| string | yes | The ID of the poker board associated with the user story being estimated. |
| jira_id | string	| yes | The Jira ID of the user story being estimated. |

## Example Usage
```
  {
    "user_name": "Scrum Team Member's Name",
    "user_id": "Scrum Team Member's ID",
    "story_point": "Assigned Story Point for User Story",
    "email": "Scrum Team Member's Email",
    "poker_board_id": "ID of the Poker Board",
    "jira_id": "ID of the User Story in JIRA"
  } 
```
## Response

 HTTP Status Code: 201 Created

| Parameter | Type | Code | Description |
| ------ | ---- |------|-------- |
| success | string |200 | A success message indicating that the estimate has been successfully submitted. |
|error | string | 400 | An error message indicating that the request was not successful. Only present in the response if an error occurred. |

## Response Body:
```
{
    "success": "Voted Successfully!"
}
```

# Libraries and Frameworks Used
- `Flask: a Python web framework`
- `Google Cloud Datastore: a NoSQL document database provided by Google Cloud Platform.`





