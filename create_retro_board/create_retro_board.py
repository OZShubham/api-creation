from flask import Flask, jsonify, redirect, request
import datetime
import random
import string
import hashlib
from google.cloud import datastore

app = Flask(__name__)

@app.route('/api/create_retro_board', methods=['POST'])
def create_retro_board():
    
    request_data = request.get_json()

    email = request_data.get('email')
    retro_board_name = request_data.get('retro_board_name')
    team_id = request_data.get('team_id')
    poker_board_id = request_data.get('poker_board_id')

    if not poker_board_id:
        return jsonify({'error': 'Please provide team_id and poker_board_id fields'}), 400

    def create_retro_board_id(user_id):
        current_time = datetime.datetime.now().strftime("%d%m%y")
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        board_id_str = user_id + current_time + random_string
        hash_value = hashlib.md5(board_id_str.encode('utf-8')).hexdigest()
        return hash_value

    retro_board_id = create_retro_board_id(email)
    client = datastore.Client()
    pokerboard_key = client.key('PokerBoard', poker_board_id)
    pokerboard_entity = client.get(pokerboard_key)

    if pokerboard_entity is not None:
        poker_board_name = pokerboard_entity.get('poker_board_name')
    else:
        poker_board_name = None

    response_dict = {
        'user_id': email,
        'retro_board_name': retro_board_name,
        'retro_board_id': retro_board_id,
        'team_id': team_id,
        'poker_board_name': poker_board_name,
        'poker_board_id': poker_board_id,
        'org_id': 'cognizant',
        'created_timestamp': datetime.datetime.utcnow(),
        'status': 'Created'
    }

    client = datastore.Client()
    entity_key = client.key('RetroBoard', retro_board_id)
    entity = datastore.Entity(key=entity_key)
    entity.update(response_dict)
    client.put(entity)

    return jsonify({'success': 'Retro Board Created Successfully!'}), 201

# Handle other request methods
@app.route('/api/create_retro_board', methods=['GET'])
def handle_invalid_methods():
    return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run()
