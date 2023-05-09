from flask import Flask, jsonify, request
import bcrypt
from google.cloud import datastore

app = Flask(__name__)

# Initialize Google Cloud Datastore client
datastore_client = datastore.Client()

@app.route('/api/signup', methods=['POST','GET'])
def signup():
    # Get form data from request
    data = request.get_json()
    name = data['name']
    user_id = data['email']
    email = data['email']
    user_role = data['user_role']
    password = data['password']
    confirm_password = data['confirm_password']

    hashed_password = bcrypt.hashpw(
        password.encode('utf-8'), bcrypt.gensalt())

    # Check if password and confirm password match
    if password != confirm_password:
        return jsonify({'error': 'Password and Confirm Password do not match'}), 400

    # Check if user already exists in Datastore
    query = datastore_client.query(kind='User')
    query.add_filter('email', '=', email)
    existing_users = query.fetch()

    if len(list(existing_users)) > 0:
        return jsonify({'error': 'User with this email already exists'}), 400

    # Save new user to Datastore
    user_key = datastore_client.key('User', user_id)
    user = datastore.Entity(key=user_key)
    user['name'] = name
    user['email'] = email
    user['user_id'] = user_id
    user['user_role'] = user_role
    user['password'] = hashed_password.decode('utf-8')
    datastore_client.put(user)

    return jsonify({'success': 'Account Created Successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
