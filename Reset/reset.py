from flask import Flask, jsonify, request
from google.cloud import datastore
import bcrypt

app = Flask(__name__)

# Initialize Google Cloud Datastore client
datastore_client = datastore.Client()

@app.route('/api/reset_password', methods=['GET', 'POST'])
def reset_password():
    data = request.get_json()
    email = data['email']
    new_password = data['new_password']

    # Check if email and new password are provided
    if not email or not new_password:
        return jsonify({'error': 'Email and new password are required'}), 400

    # Query Datastore to check if email exists
    query = datastore_client.query(kind='User')
    query.add_filter('email', '=', email)
    result = list(query.fetch())  # Convert query result to list

    # If a user with the given email is found
    if len(result) > 0:
        user = result[0]

        # Update user's password in Datastore
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        user['password'] = hashed_password.decode('utf-8') 
        datastore_client.put(user)

        return jsonify({'success': 'Password reset successfully!'}), 200

    return jsonify({'error': 'User not found'}), 404