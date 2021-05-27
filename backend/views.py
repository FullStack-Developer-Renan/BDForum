from flask import jsonify, request
from .services import CallService

def register_call_views(app):
    DATABASE = "data/banco.csv"
    @app.route('/create_message', methods=['POST'])
    def send_message():
        call_record = CallService.post_message(DATABASE, **request.json) 
        return call_record, 201

    @app.route('/messages')
    def list_messages():
        call_record = CallService.read_data(DATABASE)
        return jsonify(call_record)