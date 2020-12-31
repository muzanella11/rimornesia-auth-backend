from app import app
from app.core.controllers import BaseControllers
from app.models.model_user import ModelUser
from app.models.model_user_session import ModelUserSession
from app.services.user_service import UserService
from app.libraries.helpers import Helpers
from app.libraries.random_string import RandomString
from app.libraries.token_handler import TokenHandler
import re

class Authentication(BaseControllers):
    request = None

    TABLES = {}

    base_result = {
        'code': 200,
        'message': 'Success',
        'data': None
    }

    SESSION_TOKEN_LENGTH = 8

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

    def signin(self):
        request_data = self.request.json
        identity_signin = request_data.get('identity_signin') # You can fill with email or username
        password = request_data.get('password')
        user_data = None

        if Helpers().is_email(identity_signin):
            # Signin by email
            data_sql = getattr(ModelUser(), 'get_detail_by')('email', identity_signin, True)
            user_data = data_sql.get('data')

            if user_data:
                if password != Helpers().decrypt(user_data.get('password')):
                    errors = [
                        {
                            'field': 'identity_signin',
                            'messages': 'Credential not match'
                        },
                        {
                            'field': 'password',
                            'messages': 'Credential not match'
                        }
                    ]

                    return self.error_response(errors)
                
                del user_data['password']
            else:
                errors = [
                    {
                        'field': 'identity_signin',
                        'messages': 'Wrong email or username'
                    }
                ]

                return self.error_response(errors)
        else:
            # Signin by username
            data_sql = getattr(ModelUser(), 'get_detail_by')('username', identity_signin)
            user_data = data_sql.get('data')

            if user_data:
                if password != Helpers().decrypt(user_data.get('password')):
                    errors = [
                        {
                            'field': 'identity_signin',
                            'messages': 'Credential not match'
                        },
                        {
                            'field': 'password',
                            'messages': 'Credential not match'
                        }
                    ]

                    return self.error_response(errors)
                
                del user_data['password']
            else:
                errors = [
                    {
                        'field': 'identity_signin',
                        'messages': 'Wrong email or username'
                    }
                ]

                return self.error_response(errors)

        session_token = self.create_session()
        user_id = user_data['id']

        queries = "session_token='{}'".format(
            session_token
        )
        
        data_model = {
            'id': user_id,
            'data': queries
        }

        UserService().update_user(data_model)

        self.base_result['message'] = 'Success sign in'
        self.base_result['data'] = {
            'token': session_token
        }

        return self.create_response(self.base_result)

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

        data_token = UserService().reset_password(token, data_model)
        flag = data_token.get('flag')
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

    def create_session(self):
        session_token = self.generate_session_token()

        getattr(ModelUserSession(), 'create_data')({
            'token': session_token
        })

        session_user_id = app.mysql_lastrowid

        session_user_detail = getattr(ModelUserSession(), 'get_detail_by')('id', session_user_id)
        session_user_created = session_user_detail['data']['created_at']
        
        session_expired = TokenHandler({
            'time_by': 'minute',
            'time_by_value': 1,
            'session_time': session_user_created
        }).create_expired_time()

        queries = "expired='{}'".format(session_expired)
        
        data_model_session = {
            'id': session_user_id,
            'data': queries
        }

        getattr(ModelUserSession(), 'update_data')(data_model_session)

        return session_token

    def generate_session_token(self):
        result = ''
        amount = 8
        token = ''
        
        for item in range(amount):
            token = RandomString({
                'key_length': self.SESSION_TOKEN_LENGTH
            }).run()

            if result == '':
                result = token
            else:
                result = '{}-{}'.format(result, token)

        return result.upper()

    def whoami(self, token = None):
        whoami_data = getattr(ModelUserSession(), 'get_detail_by')('token', token)
        whoami_expired = None
        is_expired = True

        if not whoami_data['data']:
            errors = [
                {
                    'messages': 'Token not found'
                }
            ]

            return self.error_response(errors)

        if whoami_data['data']:
            whoami_expired = whoami_data['data']['expired']
            is_expired = Helpers().check_expired(whoami_expired)
            user_data = None

            if not is_expired:
                user_data_sql = UserService().generate_user_detail('session_token', token)

                user_data = user_data_sql.get('data')
        
        self.base_result['message'] = 'Success'
        self.base_result['data'] = {
            'is_expired': is_expired,
            'expired': whoami_expired,
            'whoami': user_data
        }

        return self.create_response(self.base_result)
        