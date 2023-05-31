from flask import Flask, request, jsonify
from google.cloud import datastore

app = Flask(__name__)

datastore_client = datastore.Client()

@app.route('/api/member_board', methods=['POST'])
def member_board():
    data = request.get_json()
    email = data.get('email')

    # Retrieve the user's name from Datastore
    query = datastore_client.query(kind='User')
    query.add_filter('email', '=', email)
    result = list(query.fetch())
    name = result[0]['name'] if result else None

    # Retrieve the user with the given email
    query = datastore_client.query(kind='User')
    query.add_filter('email', '=', email)
    users = list(query.fetch())

    if users:
        user = users[0]
        poker_boards = user.get('entitlement', [])
        return jsonify({'boards': poker_boards, 'name': name}), 200

    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run()
