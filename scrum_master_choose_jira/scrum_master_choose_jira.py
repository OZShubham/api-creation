from flask.views import MethodView
from flask import jsonify, request
from flask import Blueprint, render_template, url_for, request, session, redirect, Flask, jsonify, flash
import json
import datetime
import hashlib
import random
import string
from google.cloud import datastore

app = Flask(__name__)

@app.route('/choose_jira_id', methods=['GET', 'POST'])
def choose_jira_id():
    
    if request.method == "GET":
        request_data = request.get_json()

        poker_board_id = request_data.get('poker_board_id')
        client=datastore.Client()
        entity_key=client.key('newStory',poker_board_id)
        entity=client.get(entity_key)
        
        if not entity:
            
            return jsonify({'error':'There is no JIRA Title in your backlog, Please create JIRA Title first.'}), 400

        def get_backlog_story():
            
            backlog=entity.get('story',[])

            return json.dumps(backlog,indent=4, sort_keys=True, default=str)
            
        stories = get_backlog_story()
        stories_json = json.loads(stories)
        

        # Extract the jira_ids from the fetched entities
        jira_ids = []
        for story in stories_json:
            jira_title = story.get('jira_title')

            jira_id = story.get('jira_id')
            if jira_id:
                jira_ids.append({'jira_id':jira_id,'jira_title':jira_title})

        return jsonify({'jira_ids': jira_ids}), 200

    else:
        return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)