from flask import Flask, request, jsonify
from google.cloud import datastore

app = Flask(__name__)

datastore_client = datastore.Client()

@app.route('/api/choose_retro_board_member', methods=['GET', 'POST'])
def choose_retro_board_member():
    data = request.get_json()
    email = data.get('email')

    # Retrieve the user's name and retro board entitlement from Datastore
    query = datastore_client.query(kind='User')
    query.add_filter('email', '=', email)
    result = list(query.fetch())
    
    if result:
        user = result[0]
        name = user['name']
        retro_boards = user.get('retro_board_entitlement', [])

        return jsonify({'boards': retro_boards, 'name': name}), 200

    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run()
