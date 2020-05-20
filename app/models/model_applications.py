from app import app
from app.core.models import Models

class ModelApplications(Models):
    def __init__(self, params = None):
        super(ModelApplications, self).__init__(params)

        self.table_name = 'applications'

    def get_list(self):
        sql_rows = self.execute("SELECT id, name, description, url, env, `key` from `{}`".format(self.table_name))

        return sql_rows

    def get_detail_by(self, columns = None, value = None):
        if columns == "name":
            value = value.replace('-', ' ')

        sql_rows = self.execute("SELECT id, name, description, url, env, `key` from `{}` WHERE `{}` = '{}'".format(self.table_name, columns, value))

        return sql_rows

    def create_data(self, value = None):
        action = {}

        action['{}'.format(self.table_name)] = {
            'action': self.action_type.get('insert'),
            'command': (
                "INSERT INTO `{}` (`name`,`description`, `url`, `env`, `key`) VALUES".format(self.table_name) +
                " ('{}','{}','{}','{}','{}')".format(value.get('name'), value.get('description'), value.get('url'), value.get('env'), value.get('key'))
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