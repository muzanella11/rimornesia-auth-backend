from app.config.migrations import MigrationsConfig

class DatabaseStructure(object):
    ACTION = MigrationsConfig().getAction()
    TABLES = {}

    def __init__(self):
        super(DatabaseStructure, self).__init__()

    def init_structure(self):
        return self.TABLES