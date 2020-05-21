from app.core.controllers import BaseControllers
from app.core.secrets import Secrets

class Secret(BaseControllers):
    request = None
    value = None

    def __init__(self, request = None):
        super(Secret, self).__init__()

        self.request = request

    def run(self):
        data = {
            'code': 200,
            'message': 'Success',
            'data': []
        }

        return self.create_response(data)

    def generate_key(self):
        data = {
            'code': 200,
            'message': 'Success',
            'data': []
        }

        secret_value = Secrets({}).generate_key()

        data['data'] = secret_value

        return self.create_response(data)

    def encrypt(self):
        data = {
            'code': 200,
            'message': 'Success',
            'data': []
        }

        request_data = self.request.json
        self.value = request_data.get('value')

        secret_value = Secrets({
            'value': self.value
        }).encrypt()

        data['data'] = secret_value

        return self.create_response(data)

    def decrypt(self):
        data = {
            'code': 200,
            'message': 'Success',
            'data': []
        }

        request_data = self.request.json
        self.value = request_data.get('value')

        secret_value = Secrets({
            'value': self.value
        }).decrypt()

        data['data'] = secret_value

        return self.create_response(data)