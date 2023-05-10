from flask import Flask, request, jsonify
from google.cloud import datastore

app = Flask(__name__)

@app.route('/api/grant_user_access', methods=['POST'])
def grant_user_access_api():
    # Get data from JSON request
    data = request.get_json()
    email = data.get('email')

    datastore_client = datastore.Client()
    query = datastore_client.query(kind='PokerBoard')
    boards = query.fetch()

    # Get data from JSON request
    poker_board_id = data.get('poker_board_id')
    user_ids = data.get('user_ids')

    # Query Datastore for user with matching email
    query = datastore_client.query(kind='User')
    query.add_filter('email', '=', email)
    result = list(query.fetch(limit=1))
    if not result:
        return jsonify({'error': 'User not found'}), 404
    user = result[0]

    # Check if user has Scrum Master role
    if 'user_role' not in user or user['user_role'] != 'scrum_master':
        return jsonify({'error': 'User does not have Scrum Master role'}), 401

    # Get PokerBoard entity from Datastore
    poker_board_key = datastore_client.key('PokerBoard', poker_board_id)
    poker_board = datastore_client.get(poker_board_key)
    poker_board_name = poker_board.get('poker_board_name')
    poker_board_type = poker_board.get('poker_board_type')

    # Check if PokerBoard entity exists
    if not poker_board:
        return jsonify({'error': 'Poker Board does not exist'}), 404

    # Grant access to each selected user
    for user_id in user_ids:
        # Get User entity from Datastore
        user_key = datastore_client.key('User', user_id)
        user = datastore_client.get(user_key)

        # Check if User entity exists
        if not user:
            return jsonify({'error': 'User does not exist'}), 404

        # Grant access to user by adding poker_board_id to User's list of entitlement
        if 'entitlement' not in user:
            user['entitlement'] = []
        user['entitlement'].append({'poker_board_id': poker_board_id, 'poker_board_type':poker_board_type,  'poker_board_name': poker_board_name})
        datastore_client.put(user)

    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
