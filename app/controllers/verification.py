from app.core.controllers import BaseControllers
from app.models.model_user import ModelUser
from app.services.user_service import UserService
import re

class Verification(BaseControllers):
    request = None

    TABLES = {}

    def __init__(self, request = None):
        super(Verification, self).__init__()

        self.request = request

    def run(self):
        data = {
            'code': 200,
            'message': 'Success',
            'data': []
        }

        return self.create_response(data)

    def verify(self, token = None):
        data = {
            'code': 200,
            'message': 'Success',
            'data': [],
            'total_data': 0
        }

        data_verification = UserService().verification(token)
        flag = data_verification.get('flag')
        errors = []

        if (flag):
            errors.append({
                'messages': flag['message']
            })

            return self.create_response({
                'code': 400,
                'messages': 'Bad Request',
                'errors': errors
            })

        return self.create_response(data)

    def request_new_token(self):
        data = {
            'code': 200,
            'message': 'Success',
            'total_data': 0
        }

        request_data = self.request.json
        email = request_data.get('email')

        UserService().request_verification_token(email)

        return self.create_response(data)