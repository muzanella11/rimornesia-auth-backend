from app.core.migrations import Migrations
from app.migrations.seeder.seeder_provinces import SeederProvinces
from app.migrations.seeder.seeder_regencies import SeederRegencies
from app.migrations.seeder.seeder_districts import SeederDistricts
from app.migrations.seeder.seeder_villages import SeederVillages
import os

DB_NAME = os.environ.get('DB_NAME')

regencies_data = SeederRegencies().run()
districts_data = SeederDistricts().run()
villages_data = SeederVillages().run()

migrate = Migrations()
reconnect = False

# Create or Use database
migrate.create_database(DB_NAME)

reconnect = False

# Close Connection
migrate.close_connection()