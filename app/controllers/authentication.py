from app.core.controllers import BaseControllers
from app.models.model_user import ModelUser
from app.services.user_service import UserService
import re

class Authentication(BaseControllers):
    request = None

    TABLES = {}

    def __init__(self, request = None):
        super(Authentication, self).__init__()

        self.request = request

    def run(self):
        data = {
            'code': 200,
            'message': 'Success',
            'data': []
        }

        return self.create_response(data)

    def get_list(self):
        data = {
            'code': 200,
            'message': 'Success',
            'data': [],
            'total_data': 0
        }

        data_model = {
            'type': 'list',
            'pagination': True,
            'filter': self.request.args
        }

        data_sql = UserService().generate_user_list(data_model)

        data['data'] = data_sql.get('data')
        data['total_data'] = data_sql.get('total_rows')

        return self.create_response(data)

    def get_detail(self, columns = None, value = None):
        if columns == "name":
            if re.search('[_!$%^&*()_+|~=`{}\[\]:";\'<>?,.\/\s]', value):
                return self.create_response({
                    'code': 400,
                    'messages': 'Bad Request'
                })

        data = {
            'code': 200,
            'message': 'Success',
            'data': {},
            'total_data': 0
        }

        data_sql = UserService().generate_user_detail(columns, value)

        data['data'] = data_sql.get('data')
        data['total_data'] = data_sql.get('total_rows')

        return self.create_response(data)

    def create_data(self):
        data = {
            'code': 200,
            'message': 'Success'
        }

        request_data = self.request.json
        first_name = request_data.get('first_name')
        last_name = request_data.get('last_name')
        email = request_data.get('email')
        password = request_data.get('password')
        username = request_data.get('username')
        dob = request_data.get('dob')
        age = request_data.get('age')
        gender = request_data.get('gender')
        phone = request_data.get('phone')
        identity = request_data.get('identity')
        identity_type = request_data.get('identity_type')
        address = request_data.get('address')
        is_verified = 0
        roles = 4 # is role as user
        
        data_model = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'username': username,
            'dob': dob,
            'age': age,
            'gender': gender,
            'phone': phone,
            'identity': identity,
            'identity_type': identity_type,
            'address': address,
            'roles': roles,
            'is_verified': is_verified
        }

        UserService().create_user(data_model)

        return self.create_response(data)

    def reset_password(self, token = None):
        data = {
            'code': 200,
            'message': 'Success'
        }

        request_data = self.request.json
        password = request_data.get('password')
        repassword = request_data.get('repassword')

        data_model = {
            'password': password,
            'repassword': repassword
        }

        data_verification = UserService().reset_password(token, data_model)
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

    def reset_password_check(self, token = None):
        data = {
            'code': 200,
            'message': 'Success',
            'total_data': 0
        }

        data_sql = UserService().check_reset_password(token)

        data['data'] = data_sql.get('data')
        data['total_data'] = data_sql.get('total_rows')

        return self.create_response(data)


    def request_reset_password(self):
        data = {
            'code': 200,
            'message': 'Success',
            'total_data': 0
        }

        request_data = self.request.json
        email = request_data.get('email')

        UserService().request_reset_password_token(email)

        return self.create_response(data)
        