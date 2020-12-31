from flask import jsonify
import json

class BaseControllers(object):
    def __init__(self):
        super(BaseControllers, self).__init__()

    def create_response(self, data = {}):
        base_response = {
            'code': 500,
            'messages': 'Internal Server Error'
        }

        if not data.get('code'):
            data = base_response

        return (
            jsonify(**data),
            data['code']
        )

    def error_response(self, errors = []):
        # Errors attribute structure default
        base_error = [
            {
                'field': 'your_field',
                'messages': 'Your error message'
            }
        ]

        base_response = {
            'code': 400,
            'messages': 'Bad Request',
            'errors': errors
        }

        if len(errors) == 0:
            base_response['errors'] = base_error

        return self.create_response(base_response)