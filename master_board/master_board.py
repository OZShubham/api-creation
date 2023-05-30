from flask import Flask, request, jsonify
from google.cloud import datastore

app = Flask(__name__)

datastore_client = datastore.Client()

@app.route('/api/master_board', methods=['GET', 'POST'])
def master_board():
        data = request.get_json()
        # Get email and password from form data
        email = data.get('email')
        
        # Validate input
        if not email :
            return jsonify({'error': 'Invalid request payload'}), 400
        

        # Query Datastore for user with matching email
        query = datastore_client.query(kind='User')
        query.add_filter('email', '=', email)
        result = list(query.fetch(limit=1))

        if result:
             user = result[0]
             name = user.get('name')
             
             query = datastore_client.query(kind='PokerBoard')
             query.add_filter("user_id", "=", email)
             boards = query.fetch()
             boards_list = list(boards)

             return jsonify({'boards': boards_list, 'name': name})
            
            
                                  
        else:
            return jsonify ({'error': "Create a Poker Board"}),401 
        
       

if __name__ == '__main__':
    app.run()


