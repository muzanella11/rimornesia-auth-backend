from app.core.controllers import BaseControllers
from app.models.model_user_types import ModelUserTypes
import re

class UserTypes(BaseControllers):
    request = None

    TABLES = {}

    def __init__(self, request = None):
        super(UserTypes, self).__init__()

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

        data_sql = getattr(ModelUserTypes(data_model), 'get_list')()

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

        data_sql = getattr(ModelUserTypes(), 'get_detail_by')(columns, value)

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
        name = request_data.get('name')
        description = request_data.get('description')
        
        data_model = {
            'name': name,
            'description': description
        }

        getattr(ModelUserTypes(), 'create_data')(data_model)

        return self.create_response(data)

    def update_data(self, role_id = None):
        data = {
            'code': 200,
            'message': 'Success',
            'total_data': 0
        }

        request_data = self.request.json

        name = request_data.get('name')
        description = request_data.get('description')

        queries = "name='{}', description='{}'".format(name, description)
        
        data_model = {
            'id': role_id,
            'data': queries
        }

        getattr(ModelUserTypes(), 'update_data')(data_model)

        return self.create_response(data)

    def delete_data(self, role_id = None):
        data = {
            'code': 200,
            'message': 'Success',
            'total_data': 0
        }

        data_sql = getattr(ModelUserTypes(), 'delete_data')(role_id)

        return self.create_response(data)
        