# REST API code
from flask import Flask, request, jsonify
from google.cloud import datastore

app = Flask(__name__)

datastore_client = datastore.Client()

@app.route('/api/choose_retro_board_master', methods=['POST'])
def choose_retro_board_master():
    data = request.get_json()
    email = data.get('email')
    poker_board_id = data.get('poker_board_id')
    
    if not email or not poker_board_id:
        return jsonify({'error': 'Invalid request payload'}), 400

    query = datastore_client.query(kind='User')
    query.add_filter('email', '=', email)
    result = list(query.fetch(limit=1))

    if result:
        user = result[0]
        name = user.get('name')

        query = datastore_client.query(kind='RetroBoard')
        query.add_filter("user_id", "=", email)
        query.add_filter("poker_board_id", "=", poker_board_id)
        retro_boards = query.fetch()
        boards_list = list(retro_boards)

        retro_board_names = [board['retro_board_name'] for board in boards_list]  # Extract retro board names

        return jsonify({'retro_board_names': retro_board_names, 'name': name})  # Return retro board names
            
    else:
        return jsonify({'error': "Create a Retro Board"}), 401


if __name__ == '__main__':
    app.run()
