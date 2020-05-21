from app.core.controllers import BaseControllers
from app.models.model_access_control import ModelAccessControl
import re

class AccessControl(BaseControllers):
    request = None

    TABLES = {}

    def __init__(self, request = None):
        super(AccessControl, self).__init__()

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

        data_sql = getattr(ModelAccessControl(data_model), 'get_list')()

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

        data_sql = getattr(ModelAccessControl(), 'get_detail_by')(columns, value)

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
        role_id = request_data.get('role_id')
        apps_permission = request_data.get('apps_permission')

        if len(apps_permission) > 0:
            apps_permission = [str(x) for x in apps_permission]
            apps_permission = ','.join(apps_permission)

        data_model = {
            'role_id': role_id,
            'apps_permission': apps_permission
        }

        getattr(ModelAccessControl(), 'create_data')(data_model)

        return self.create_response(data)

    def update_data(self, application_id = None):
        data = {
            'code': 200,
            'message': 'Success',
            'total_data': 0
        }

        request_data = self.request.json

        role_id = request_data.get('role_id')
        apps_permission = request_data.get('apps_permission')

        if len(apps_permission) > 0:
            apps_permission = [str(x) for x in apps_permission]
            apps_permission = ','.join(apps_permission)

        queries = "role_id='{}', apps_permission='{}'".format(role_id, apps_permission)

        data_model = {
            'id': application_id,
            'data': queries
        }

        getattr(ModelAccessControl(), 'update_data')(data_model)

        return self.create_response(data)

    def delete_data(self, application_id = None):
        data = {
            'code': 200,
            'message': 'Success',
            'total_data': 0
        }

        data_sql = getattr(ModelAccessControl(), 'delete_data')(application_id)

        return self.create_response(data)
        