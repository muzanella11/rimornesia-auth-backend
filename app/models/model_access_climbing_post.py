from app import app
from app.core.models import Models

class ModelAccessClimbingPost(Models):
    def __init__(self, params = None):
        super(ModelAccessClimbingPost, self).__init__(params)

        self.table_name = 'access_climbing_post'

    def get_list(self):
        sql_rows = self.execute("SELECT \
        id, \
        key_access, \
        user_id, \
        climbing_post_id, \
        is_active, \
        is_owner, \
        {}, {} from `{}`".format(self.convert_time_zone('created_at'), self.convert_time_zone('updated_at'), self.table_name))

        result = []

        if sql_rows['data']:
            for item in sql_rows['data']:
                if item['is_active'] == 1:
                    item['is_active'] = True
                else:
                    item['is_active'] = False

                if item['is_owner'] == 1:
                    item['is_owner'] = True
                else:
                    item['is_owner'] = False

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

        sql_rows = self.execute("SELECT \
        id, \
        key_access, \
        user_id, \
        climbing_post_id, \
        is_active, \
        is_owner, \
        {}, {} from `{}` WHERE `{}` = '{}'".format(self.convert_time_zone('created_at'), self.convert_time_zone('updated_at'), self.table_name, columns, value))

        if sql_rows['data']:
            if sql_rows['data']['is_active'] == 1:
                sql_rows['data']['is_active'] = True
            else:
                sql_rows['data']['is_active'] = False

            if sql_rows['data']['is_owner'] == 1:
                sql_rows['data']['is_owner'] = True
            else:
                sql_rows['data']['is_owner'] = False
        
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
                "INSERT INTO `{}` (`key_access`, `user_id`, `climbing_post_id`, `is_active`, `is_owner`, `created_at`) VALUES".format(self.table_name) +
                " ('{}', '{}', '{}', '{}', '{}', NOW())".format(value.get('key_access'), value.get('user_id'), value.get('climbing_post_id'), value.get('is_active'), value.get('is_owner'))
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
                "UPDATE `{}` SET {}, updated_at=NOW() WHERE key_access='{}'".format(self.table_name, value.get('data'), value.get('key_access'))
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