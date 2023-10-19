from flask import Flask, jsonify, redirect, request
import datetime
import random
import string
import hashlib
from google.cloud import datastore

app = Flask(__name__)


@app.route('/api/scrum_team_retro_view', methods=['POST'])
def scrum_team_retro_view():

    request_data = request.get_json()

    retro_board_id = request_data.get('retro_board_id')

    client = datastore.Client()

    entity_key = client.key('RetroBoard', retro_board_id)
    entity = client.get(entity_key)
    if not entity:
        return jsonify({'error': 'Retro Board with this retro_board_id not found'}), 404

    user_id = request_data.get('email')

    what_went_well = request_data.get('what_went_well')
    what_went_wrong = request_data.get('what_went_wrong')
    what_can_be_improved = request_data.get('what_can_be_improved')

    # Check if the PokerBoard entity has a 'users' property
    if 'users' not in entity:
        entity['users'] = []

    # Find the user's data dictionary or create a new one
    user_data = next(
        (data for data in entity['users'] if user_id in data), {})
    user_data[user_id] = {
        'what_went_well': what_went_well,
        'what_went_wrong': what_went_wrong,
        'what_can_be_improved': what_can_be_improved
    }

    # Update the user's data in the PokerBoard entity
    if user_data not in entity['users']:
        entity['users'].append(user_data)

    client.put(entity)
    return jsonify({'success': 'Team member data sent successfully!'}), 201

# Handle other request methods


@app.route('/api/scrum_team_retro_view', methods=['GET'])
def handle_invalid_methods():
    return jsonify({'error': 'Method not allowed'}), 405


if __name__ == '__main__':
    app.run()
