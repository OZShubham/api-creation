from flask import Flask, request, jsonify
import bcrypt
from google.cloud import datastore

app = Flask(__name__)

datastore_client = datastore.Client()

@app.route('/api/login', methods=['GET', 'POST'])
def login():
        data = request.get_json()
        # Get email and password from form data
        email = data.get('email')
        password = data.get('password')
        # Validate input
        if not email  and not password:
            return jsonify({'error': 'Invalid request payload'}), 400
        

        # Query Datastore for user with matching email
        query = datastore_client.query(kind='User')
        query.add_filter('email', '=', email)
        result = list(query.fetch(limit=1))

        if result:
            # User found, retrieve hashed password
            user = result[0]
            hashed_password = user['password'].encode('utf-8')

            # Validate password
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                # Passwords match, log in user
                
               return jsonify ({"message": "User logged in successfully"}), 200
                                
            else:
                # Incorrect password
                return jsonify ({'error': "Incorrect Password"}),401 

               
                
        else:
             return jsonify({'error': 'User not found'}), 404
    
    
if __name__ == '__main__':
    app.run()
