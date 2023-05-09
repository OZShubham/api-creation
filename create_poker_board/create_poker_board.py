from flask.views import MethodView
from flask import jsonify, request
from flask import Blueprint, render_template, url_for, request, session, redirect, Flask, jsonify, flash
import json
import datetime
import hashlib
import random
import string
from google.cloud import datastore

app = Flask(__name__)

@app.route('/api/create_poker_board', methods=['GET', 'POST'])
def create_poker_board():
    if request.method == 'POST':
        data = request.get_json()

        email = data['email']
        poker_board_name = data['poker_board_name']
        team_id = data['team_id']
        poker_board_type = data['poker_board_type']

        if not team_id or not poker_board_type or not poker_board_name or not email:
            return jsonify({'error': 'Bad Request. Please fill all the fields correctly.'}), 400

        
        def create_board_id(user_id):
            current_time = datetime.datetime.now().strftime("%d%m%y")
            # Generate a random string of length 8
            random_string = ''.join(random.choices(
                string.ascii_letters + string.digits, k=8))
            board_id_str = user_id + current_time + random_string
            hash_value = hashlib.md5(board_id_str.encode('utf-8')).hexdigest()
            return hash_value

        poker_board_id = create_board_id(email)

        response_dict = {
            'user_id': email,
            'poker_board_name': poker_board_name,
            'poker_board_id': poker_board_id,
            'poker_board_type': poker_board_type,
            'org_id': 'cognizant',
            'created_timestamp': datetime.datetime.utcnow(),
            'last_modified_timestamp': datetime.datetime.utcnow(),
            'team_id': team_id,
            'status': 'Created'
        }

        # Save response_dict to Datastore
        client = datastore.Client()
        entity_key = client.key('PokerBoard', poker_board_id)
        entity = datastore.Entity(key=entity_key)
        entity.update(response_dict)
        client.put(entity)

        return jsonify({'success': 'Poker Board Created Successfully!'}), 201

    # Return a default response for other request methods
    return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)