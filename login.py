from flask import Flask, jsonify, request,session,redirect,render_template,flash
import bcrypt
from google.cloud import datastore

app = Flask(__name__)

# Initialize Google Cloud Datastore client
datastore_client = datastore.Client()

@app.route('/api/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        email = data['email']
        password = data['password']

        try:
            # Retrieve user entity from Datastore based on email
            query = datastore_client.query(kind='User')
            query.add_filter('email', '=', email)
            result = list(query.fetch(limit=1))

            if result:
                user = result[0]
                
                # Retrieve hashed password from Datastore
                hashed_password = user['password'].encode('utf-8')

                # Verify input password with hashed password
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                    # Passwords match, return success
                    return jsonify({'success': True,
                                'message': 'Sign-in successful'}), 201
                    
                else:
                    # Passwords don't match, return error
                    flash("Incorrect Password!", "info")
                    return redirect('/login')
            else:
                # User not found, return error
                flash("Incorrect Email!", "info")
                return redirect('/login')
        except Exception as e:
            print('Error:', e)
            # Return error response
            return jsonify({'success': False, 'message': 'Login unsuccessful'}), 203

        
     # Return a default response for other request methods
    return jsonify({'error': 'Method not allowed'}), 405


if __name__ == '__main__':
    app.run(debug=True)