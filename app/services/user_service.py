from app import app
from app.libraries.random_string import RandomString
from app.libraries.token_handler import TokenHandler
from app.models.model_user import ModelUser
from app.models.model_user_identity_types import ModelUserIdentityTypes
from app.models.model_user_verification_session import ModelUserVerificationSession
from app.models.model_user_reset_password_session import ModelUserResetPasswordSession
from app.core.secrets import Secrets

class UserService(object):
    config = {}
    base_result = {
        'data': None,
        'total_data': 0
    }
    VERIFICATION_TOKEN_LENGTH = 8
    
    def __init__(self, config = None):
        super(UserService, self).__init__()

        if config:
            self.config = config

    def generate_user_list(self, data_model = None):
        data_sql = getattr(ModelUser(data_model), 'get_list')()

        raw_data = data_sql.get('data')

        if raw_data:
            for item_raw_data in raw_data:
                # Get user identity type value
                data_type = item_raw_data.get('identity_type')

                content_data = getattr(ModelUserIdentityTypes(), 'get_detail_by')('id', data_type)
                content_data = content_data.get('data')

                item_raw_data['identity_label'] = content_data.get('label')
                

        self.base_result['data'] = data_sql.get('data')
        self.base_result['total_data'] = data_sql.get('total_rows')

        return self.base_result

    def generate_user_detail(self, columns = None, booking_code = None):
        data_sql = getattr(ModelUser(), 'get_detail_by')(columns, booking_code)

        raw_data = data_sql.get('data')

        if raw_data:
            # Get user identity type value
            data_type = raw_data.get('identity_type')

            content_data = getattr(ModelUserIdentityTypes(), 'get_detail_by')('id', data_type)
            content_data = content_data.get('data')
            
            raw_data['identity_label'] = content_data.get('label')

        self.base_result['data'] = data_sql.get('data')
        self.base_result['total_data'] = data_sql.get('total_rows')

        return self.base_result

    def create_user(self, data_model = None):
        # To Do :: Create validation here

        # Encrypt password
        password = Secrets({
            'value': data_model['password']
        }).encrypt()

        data_model['password'] = password

        # Verification token
        verification_token = self.create_verification()
        data_model['verification_token'] = verification_token

        getattr(ModelUser(), 'create_data')(data_model)

    def update_user(self, data_model = None):
        # To Do :: Create validation here

        getattr(ModelUser(), 'update_data')(data_model)

    def create_display_name(self, first_name = None, last_name = None):
        return '{} {}'.format(first_name, last_name)

    def delete_user(self, user_id = None):
        # To Do :: Create validation here
        getattr(ModelUser(), 'delete_data')(user_id)

    def generate_verification_token(self):
        result = ''
        amount = 8
        token = ''
        
        for item in range(amount):
            token = RandomString({
                'key_length': self.VERIFICATION_TOKEN_LENGTH
            }).run()

            if result == '':
                result = token
            else:
                result = '{}-{}'.format(result, token)

        return result.upper()

    def verification(self, token):
        token_data = getattr(ModelUserVerificationSession(), 'get_detail_by')('token', token)
        expired = None

        if token_data['data']:
            expired = token_data['data']['expired']

        is_expired = self.check_expired(expired)

        if (is_expired):
            self.base_result['flag'] = {
                'message': 'Token is expired'
            }

            return self.base_result

        user_data = getattr(ModelUser(), 'get_detail_by')('verification_token', token)
        user_id = user_data['data']['id']

        queries = "is_verified='{}'".format(1)
        
        data_model_user = {
            'id': user_id,
            'data': queries
        }

        getattr(ModelUser(), 'update_data')(data_model_user)

        return self.base_result

    def create_verification(self):
        verification_token = self.generate_verification_token()

        getattr(ModelUserVerificationSession(), 'create_data')({
            'token': verification_token
        })

        verification_session_id = app.mysql_lastrowid

        verification_session_detail = getattr(ModelUserVerificationSession(), 'get_detail_by')('id', verification_session_id)
        verification_session_created = verification_session_detail['data']['created_at']
        
        verification_expired = TokenHandler({
            'time_by': 'minute',
            'time_by_value': 30,
            'session_time': verification_session_created
        }).create_expired_time()

        queries = "expired='{}'".format(verification_expired)
        
        data_model_session = {
            'id': verification_session_id,
            'data': queries
        }

        getattr(ModelUserVerificationSession(), 'update_data')(data_model_session)

        return verification_token

    def request_verification_token(self, email = None):
        # Verification token
        token = self.create_verification()

        user_data = getattr(ModelUser(), 'get_detail_by')('email', email)
        user_id = user_data['data']['id']

        queries = "verification_token='{}'".format(token)
        
        data_model_user = {
            'id': user_id,
            'data': queries
        }

        getattr(ModelUser(), 'update_data')(data_model_user)


    def check_expired(self, expired_time = None):
        return TokenHandler().check_expired_time(expired_time)

    def create_reset_password(self, user_id = None):
        verification_token = self.generate_verification_token()

        getattr(ModelUserResetPasswordSession(), 'create_data')({
            'token': verification_token,
            'user_id': user_id
        })

        verification_session_id = app.mysql_lastrowid

        verification_session_detail = getattr(ModelUserResetPasswordSession(), 'get_detail_by')('id', verification_session_id)
        verification_session_created = verification_session_detail['data']['created_at']
        
        verification_expired = TokenHandler({
            'time_by': 'minute',
            'time_by_value': 10,
            'session_time': verification_session_created
        }).create_expired_time()

        queries = "expired='{}'".format(verification_expired)
        
        data_model_session = {
            'id': verification_session_id,
            'data': queries
        }

        getattr(ModelUserResetPasswordSession(), 'update_data')(data_model_session)

        return verification_token

    def request_reset_password_token(self, email = None):
        user_data = getattr(ModelUser(), 'get_detail_by')('email', email)
        user_id = user_data['data']['id']

        # Verification token
        token = self.create_reset_password(user_id)

    def check_reset_password(self, token = None):
        reset_password_data = getattr(ModelUserResetPasswordSession(), 'get_detail_by')('token', token)
        reset_password_expired = None
        is_expired = True

        if reset_password_data['data']:
            reset_password_expired = reset_password_data['data']['expired']
            is_expired = self.check_expired(reset_password_expired)
        
        self.base_result['data'] = {
            'is_expired': is_expired,
            'expired': reset_password_expired
        }

        return self.base_result

    def reset_password(self, token = None, data_model = None):
        token_data = getattr(ModelUserResetPasswordSession(), 'get_detail_by')('token', token)
        expired = None
        user_id = None

        if token_data['data']:
            expired = token_data['data']['expired']
            user_id = token_data['data']['user_id']

        is_expired = self.check_expired(expired)
        password = data_model['password']

        if is_expired:
            self.base_result['flag'] = {
                'message': 'Token is expired'
            }

            return self.base_result

        if not password:
            self.base_result['flag'] = {
                'message': 'Password is required'
            }

            return self.base_result

        # Encrypt password
        password = Secrets({
            'value': password
        }).encrypt()

        queries = "password='{}'".format(password)
        
        data_model_user = {
            'id': user_id,
            'data': queries
        }

        getattr(ModelUser(), 'update_data')(data_model_user)

        return self.base_result