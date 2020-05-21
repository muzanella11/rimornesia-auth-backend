from flask import request
from app import app
from app.controllers.health_indicator import HealthIndicator
from app.controllers.secret import Secret
from app.controllers.user_roles import UserRoles
from app.controllers.applications import Applications
from app.controllers.access_control import AccessControl

@app.route('/api')
def helloapi():
    return "Hello World!"
## Health Check ##
@app.route('/health')
def health_indicator():
    return HealthIndicator().run()
##################

## Secret ##
@app.route('/secret/key', methods=['GET'])
def secret_key():
    return Secret(request).generate_key()

@app.route('/secret/encrypt', methods=['POST'])
def secret_key_encrypt():
    return Secret(request).encrypt()

@app.route('/secret/decrypt', methods=['POST'])
def secret_key_decrypt():
    return Secret(request).decrypt()
##################

## User Roles ##
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
##################

## Applications ##
@app.route('/application')
def applicationlistapi():
    return Applications(request).get_list()

@app.route('/application/<value>')
def applicationdetailapi(value):
    if value.isnumeric():
        return Applications(request).get_detail('id', value)

    return Applications(request).get_detail('name', value)

@app.route('/application', methods=['POST'])
def applicationcreateapi():
    return Applications(request).create_data()

@app.route('/application/<id>', methods=['PUT'])
def applicationupdateapi(id):
    return Applications(request).update_data(id)

@app.route('/application/<id>', methods=['DELETE'])
def applicationdeleteapi(id):
    return Applications(request).delete_data(id)
##################

## Access Control ##
@app.route('/access-control')
def accesscontrollistapi():
    return AccessControl(request).get_list()

@app.route('/access-control/<value>')
def accesscontroldetailapi(value):
    if value.isnumeric():
        return AccessControl(request).get_detail('id', value)

    return AccessControl(request).get_detail('name', value)

@app.route('/access-control', methods=['POST'])
def accesscontrolcreateapi():
    return AccessControl(request).create_data()

@app.route('/access-control/<id>', methods=['PUT'])
def accesscontrolupdateapi(id):
    return AccessControl(request).update_data(id)

@app.route('/access-control/<id>', methods=['DELETE'])
def accesscontroldeleteapi(id):
    return AccessControl(request).delete_data(id)
##################