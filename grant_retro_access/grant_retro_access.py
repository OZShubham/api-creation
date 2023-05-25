from flask import Flask, request, jsonify, redirect
from google.cloud import datastore

app = Flask(__name__)

@app.route('/api/grant_retro_access', methods=['POST'])
def grant_retro_access_api():
    # Get data from JSON request
    data = request.get_json()
    email = data.get('email')
    retro_board_id = data.get('retro_board_id')
    user_ids = data.get('user_ids')

    datastore_client = datastore.Client()

    # Query Datastore for user with matching email
    query = datastore_client.query(kind='User')
    query.add_filter('email', '=', email)
    result = list(query.fetch(limit=1))
    if not result:
        return jsonify({'error': 'User not found'}), 404
    user = result[0]

    # Check if user has Scrum Master role
    if user['email'] != email:
        return jsonify({'error': 'User does not have Scrum Master role'}), 401

    # Get RetroBoard entity from Datastore
    retro_board_key = datastore_client.key('RetroBoard', retro_board_id)
    retro_board = datastore_client.get(retro_board_key)
    retro_board_name = retro_board.get('retro_board_name')

    # Check if RetroBoard entity exists
    if not retro_board:
        return jsonify({'error': 'Retro Board does not exist'}), 404

    # Grant access to each selected user
    for user_id in user_ids:
        # Get User entity from Datastore
        user_key = datastore_client.key('User', user_id)
        user = datastore_client.get(user_key)

        # Check if User entity exists
        if not user:
            return jsonify({'error': 'User does not exist'}), 404

        # Check if the user already has access to the retro board
        retro_board_entitlements = user.get('retro_board_entitlement', [])
        retro_board_exists = any(
            entitlement.get('retro_board_id') == retro_board_id for entitlement in retro_board_entitlements
        )
        if retro_board_exists:
            continue  # Skip granting access to this user

        # Grant access to user by adding retro_board_id to User's list of entitlement
        retro_board_entitlements.append({'retro_board_id': retro_board_id, 'retro_board_name': retro_board_name})
        user['retro_board_entitlement'] = retro_board_entitlements
        datastore_client.put(user)

    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
