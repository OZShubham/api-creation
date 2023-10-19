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


@app.route('/api/scrum_team_member_view', methods=['GET', 'POST'])
def scrum_team_member_view():

    data = request.get_json()

    name = data['user_name']
    user_id = data['user_id']
    story_point = data['story_point']
    email = data['email']
    poker_board_id = data['poker_board_id']
    jira_id = data['jira_id']

    # Validate input data
    if not poker_board_id or not jira_id or not user_id:
        return jsonify({'error': 'Bad Request. Please provide all the fields. i.e. jira_id, poker_board_id, user_id'}), 400

    # Query Datastore for user with matching email
    client = datastore.Client()
    query = client.query(kind='User')
    query.add_filter('email', '=', email)
    result = list(query.fetch(limit=1))
    if not result:
        return jsonify({'Error', "User is not Found."}), 404

    # Update PokerBoard entity
    entity_key = client.key('PokerBoard', poker_board_id)
    entity = client.get(entity_key)
    if not entity:
        return jsonify({'Error', "'No entity found with this poker_board_id"}), 404

    user_id = session.get('email')
    story_point = request.form.get('story_point')
    updated_estimate = False
    updated_user = False
    estimates = entity.get('estimates', [])

    for estimate in estimates:
        if estimate.get('jira_id') == jira_id:
            users = estimate.get('users', [])

            for user in users:
                if user.get('user_id') == user_id:
                    user['story_point'] = story_point
                    user['user_name'] = name
                    user['created_timestamp'] = datetime.datetime.utcnow()
                    updated_user = True
                    updated_estimate = True
                    break

            if not updated_user:
                users.append({'user_id': user_id, 'user_name': name, 'story_point': story_point,
                              'created_timestamp': datetime.datetime.utcnow()})
                estimate['users'] = users
                updated_estimate = True
            break

    if not updated_estimate:
        estimates.append({'jira_id': jira_id, 'users': [{'user_id': user_id, 'user_name':name, 'story_point': story_point,
                                                             'created_timestamp': datetime.datetime.utcnow()}]})

    entity.update({'estimates': estimates,
                    'last_modified_timestamp': datetime.datetime.utcnow()})
    client.put(entity)
    return jsonify({'success': 'Voted Successfully!'}), 201
