from app import app
from app.core.models import Models

class ModelAccessControl(Models):
    def __init__(self, params = None):
        super(ModelAccessControl, self).__init__(params)

        self.table_name = 'access_controls'

    def get_list(self):
        sql_rows = self.execute("SELECT id, role_id, apps_permission, {}, {} from `{}`".format(self.convert_time_zone('created_at'), self.convert_time_zone('updated_at'), self.table_name))

        result = []

        for item in sql_rows['data']:
            item['apps_permission'] = [int(x) for x in item.get('apps_permission').split(',')]

            result.append(item)

        sql_rows['data'] = result

        convert_attribute_list = [
            'created_at',
            'updated_at'
        ]

        sql_rows = self.convert_to_normal_date(sql_rows, convert_attribute_list)

        return sql_rows

    def get_detail_by(self, columns = None, value = None):
        if columns == "name":
            value = value.replace('-', ' ')

        sql_rows = self.execute("SELECT id, role_id, apps_permission, {}, {} from `{}` WHERE `{}` = '{}'".format(self.convert_time_zone('created_at'), self.convert_time_zone('updated_at'), self.table_name, columns, value))

        if sql_rows['data']:
            sql_rows['data']['apps_permission'] = [int(x) for x in sql_rows['data'].get('apps_permission').split(',')]
        
        convert_attribute_list = [
            'created_at',
            'updated_at'
        ]

        sql_rows = self.convert_to_normal_date(sql_rows, convert_attribute_list)

        return sql_rows

    def create_data(self, value = None):
        action = {}

        action['{}'.format(self.table_name)] = {
            'action': self.action_type.get('insert'),
            'command': (
                "INSERT INTO `{}` (`role_id`,`apps_permission`, `created_at`) VALUES".format(self.table_name) +
                " ('{}','{}', NOW())".format(value.get('role_id'), value.get('apps_permission'))
            )
        }

        self.execute_command(
            action
        )

    def update_data(self, value):
        action = {}

        action['{}'.format(self.table_name)] = {
            'action': self.action_type.get('update'),
            'command': (
                "UPDATE `{}` SET {}, updated_at=NOW() WHERE id={}".format(self.table_name, value.get('data'), value.get('id'))
            )
        }

        self.execute_command(
            action
        )

    def delete_data(self, value):
        action = {}

        action['{}'.format(self.table_name)] = {
            'action': self.action_type.get('delete'),
            'command': (
                "DELETE FROM `{}` WHERE id={}".format(self.table_name, value)
            )
        }

        self.execute_command(
            action
        )