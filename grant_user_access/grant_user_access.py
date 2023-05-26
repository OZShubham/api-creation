from flask import Flask, request, jsonify
from google.cloud import datastore

app = Flask(__name__)

@app.route('/api/grant_user_access', methods=['GET','POST'])
def grant_user_access():
    email = request.json.get('email')
    poker_board_id = request.json.get('poker_board_id')
    user_id_list = request.json.get('user_id_list', [])

    # Check if 'email', 'poker_board_id', and 'user_id_list' are present in the request JSON
    if not email or not poker_board_id or not user_id_list:
        return jsonify({'error': 'Invalid request payload'}), 400

    datastore_client = datastore.Client()

    query = datastore_client.query(kind='User')
    query.add_filter('email', '=', email)
    result = list(query.fetch(limit=1))

    if not result:
        return jsonify({'error': 'User not found'}), 404

    user = result[0]

    if user['email'] != email:
        return jsonify({'error': 'Unauthorized'}), 401

    poker_board_key = datastore_client.key('PokerBoard', poker_board_id)
    poker_board = datastore_client.get(poker_board_key)

    if not poker_board:
        return jsonify({'error': 'Poker Board does not exist'}), 404

    for user_id in user_id_list:
        user_key = datastore_client.key('User', user_id)
        user = datastore_client.get(user_key)

        if not user:
            return jsonify({'error': f'User {user_id} not found'}), 404

        poker_board_entitlements = user.get('entitlement', [])
        poker_board_exists = any(
            entitlement.get('poker_board_id') == poker_board_id for entitlement in poker_board_entitlements
        )

        if poker_board_exists:
            continue  # Skip granting access to this user

        if 'entitlement' not in user:
            user['entitlement'] = []

        user['entitlement'].append({'poker_board_id': poker_board_id})
        datastore_client.put(user)

    return jsonify({'message': 'Access granted successfully'})

if __name__ == '__main__':
    app.run()
