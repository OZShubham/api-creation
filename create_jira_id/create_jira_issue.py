from flask import Flask, request, jsonify
from google.cloud import datastore
import datetime

app = Flask(__name__)

# Initialize Google Cloud Datastore client
datastore_client = datastore.Client()

@app.route('/api/create_jira_id', methods=['POST'])
def create_jira_id():
    data = request.get_json()
    poker_board_id = data['poker_board_id']
    jira_id = data['jira_id']
    jira_description = data['jira_description']
    jira_title = data['jira_title']

    if not poker_board_id or not jira_id or not jira_description or not jira_title:
        return jsonify(error='Missing required fields'), 400

    client = datastore.Client()
    entity_key = client.key('PokerBoard', poker_board_id)
    entity = client.get(entity_key)

    if not entity:
        return jsonify(error='Poker board not found'), 404

    estimates = entity.get('estimates', [])
    estimates.append({
        'jira_id': jira_id,
        'jira_description': jira_description
    })
    entity.update({
        'estimates': estimates,
        'last_modified_timestamp': datetime.datetime.utcnow()
    })
    client.put(entity)

    new_story_key = client.key('newStory', poker_board_id)
    new_story_entity = datastore.Entity(key=new_story_key)
    new_story_entity.update({
        'story': [{
            'jira_id': jira_id,
            'jira_description': jira_description,
            'jira_title': jira_title,
            'created_timestamp': datetime.datetime.utcnow(),
            'last_modified_timestamp': datetime.datetime.utcnow()
        }],
        'poker_board_id': poker_board_id
    })
    client.put(new_story_entity)

    

    return jsonify(success=True), 200


if __name__ == '__main__':
    app.run(debug=True)
