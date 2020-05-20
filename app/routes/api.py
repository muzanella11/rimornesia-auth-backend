from flask import request
from app import app
from app.controllers.health_indicator import HealthIndicator
from app.controllers.secret import Secret
from app.controllers.user_roles import UserRoles

@app.route('/api')
def helloapi():
    return "Hello World!"

@app.route('/health')
def health_indicator():
    return HealthIndicator().run()

@app.route('/secret/key', methods=['GET'])
def secret_key():
    return Secret(request).generate_key()

@app.route('/secret/encrypt', methods=['POST'])
def secret_key_encrypt():
    return Secret(request).encrypt()

@app.route('/secret/decrypt', methods=['POST'])
def secret_key_decrypt():
    return Secret(request).decrypt()

@app.route('/user/role')
def rolelistapi():
    return UserRoles(request).get_list()

@app.route('/user/role/<value>')
def roledetailapi(value):
    if value.isnumeric():
        return UserRoles(request).get_detail('id', value)

    return UserRoles(request).get_detail('name', value)

@app.route('/user/role', methods=['POST'])
def rolecreateapi():
    return UserRoles(request).create_data()

@app.route('/user/role/<id>', methods=['PUT'])
def roleupdateapi(id):
    return UserRoles(request).update_data(id)

@app.route('/user/role/<id>', methods=['DELETE'])
def roledeleteapi(id):
    return UserRoles(request).delete_data(id)