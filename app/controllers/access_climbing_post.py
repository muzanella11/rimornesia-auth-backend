from app.core.controllers import BaseControllers
from app.models.model_access_climbing_post import ModelAccessClimbingPost
from app.models.model_user import ModelUser
from app.libraries.random_string import RandomString
import re

class AccessClimbingPost(BaseControllers):
    request = None

    TABLES = {}

    base_result = {
        'data': None,
        'total_data': 0
    }
    ACCESS_KEY_LENGTH = 8

    def __init__(self, request = None):
        super(AccessClimbingPost, self).__init__()

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

        data_sql = getattr(ModelAccessClimbingPost(data_model), 'get_list')()

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

        data_sql = getattr(ModelAccessClimbingPost(), 'get_detail_by')(columns, value)

        data['data'] = data_sql.get('data')
        data['total_data'] = data_sql.get('total_rows')

        return self.create_response(data)

    def create_data(self):
        data = {
            'code': 200,
            'message': 'Success',
            'total_data': 0
        }

        request_data = self.request.json
        user_id = request_data.get('user_id')
        is_active = request_data.get('is_active')
        is_owner = request_data.get('is_owner')
        climbing_post_id = request_data.get('climbing_post_id')
        key_access = self.generate_access_key()

        is_active = self.check_is_active(is_active)
        is_owner = self.check_is_owner(is_owner)

        data_model = {
            'user_id': user_id,
            'climbing_post_id': climbing_post_id,
            'is_active': is_active,
            'is_owner': is_owner,
            'key_access': key_access
        }

        getattr(ModelAccessClimbingPost(), 'create_data')(data_model)
        
        # Add key access in User
        queries = "key_access_climbing_post='{}'".format(
            key_access
        )
        
        data_model = {
            'id': user_id,
            'data': queries
        }

        getattr(ModelUser(), 'update_data')(data_model)

        return self.create_response(data)

    def update_data(self, key_access = None):
        data = {
            'code': 200,
            'message': 'Success',
            'total_data': 0
        }

        request_data = self.request.json

        is_active = request_data.get('is_active')
        is_owner = request_data.get('is_owner')
        climbing_post_id = request_data.get('climbing_post_id')

        is_active = self.check_is_active(is_active)
        is_owner = self.check_is_owner(is_owner)

        queries = "is_active='{}', is_owner='{}', climbing_post_id='{}'".format(is_active, is_owner, climbing_post_id)

        data_model = {
            'key_access': key_access,
            'data': queries
        }

        getattr(ModelAccessClimbingPost(), 'update_data')(data_model)

        return self.create_response(data)

    def delete_data(self, application_id = None):
        data = {
            'code': 200,
            'message': 'Success',
            'total_data': 0
        }

        data_sql = getattr(ModelAccessClimbingPost(), 'delete_data')(application_id)

        return self.create_response(data)

    def generate_access_key(self):
        result = ''
        amount = 8
        token = ''
        
        for item in range(amount):
            token = RandomString({
                'key_length': self.ACCESS_KEY_LENGTH
            }).run()

            if result == '':
                result = token
            else:
                result = '{}-{}'.format(result, token)

        return result.upper()

    def check_is_active(self, value):
        result = 0

        if value == True:
            result = 1

        return result

    def check_is_owner(self, value):
        result = 0

        if value == True:
            result = 1

        return result
        