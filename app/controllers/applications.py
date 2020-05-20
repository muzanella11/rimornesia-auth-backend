from app.core.controllers import BaseControllers
from app.models.model_applications import ModelApplications
import re

class Applications(BaseControllers):
    request = None

    TABLES = {}

    def __init__(self, request = None):
        super(Applications, self).__init__()

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

        data_sql = getattr(ModelApplications(data_model), 'get_list')()

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

        data_sql = getattr(ModelApplications(), 'get_detail_by')(columns, value)

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
        url = request_data.get('url')
        env = request_data.get('env')
        key = request_data.get('key')
        
        data_model = {
            'name': name,
            'description': description,
            'url': url,
            'env': env,
            'key': key
        }

        getattr(ModelApplications(), 'create_data')(data_model)

        return self.create_response(data)

    def update_data(self, application_id = None):
        data = {
            'code': 200,
            'message': 'Success',
            'total_data': 0
        }

        request_data = self.request.json

        name = request_data.get('name')
        description = request_data.get('description')
        url = request_data.get('url')
        env = request_data.get('env')
        key = request_data.get('key')

        queries = "name='{}', description='{}', url='{}', key='{}'".format(name, description, url, env, key)
        
        data_model = {
            'id': application_id,
            'data': queries
        }

        getattr(ModelApplications(), 'update_data')(data_model)

        return self.create_response(data)

    def delete_data(self, application_id = None):
        data = {
            'code': 200,
            'message': 'Success',
            'total_data': 0
        }

        data_sql = getattr(ModelApplications(), 'delete_data')(application_id)

        return self.create_response(data)
        