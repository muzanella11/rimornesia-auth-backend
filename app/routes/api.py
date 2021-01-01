from flask import request
from app import app
from app.controllers.health_indicator import HealthIndicator
from app.controllers.secret import Secret
from app.controllers.user_roles import UserRoles
from app.controllers.applications import Applications
from app.controllers.access_control import AccessControl
from app.controllers.user_types import UserTypes
from app.controllers.user_identity_types import UserIdentityTypes
from app.controllers.users import Users
from app.controllers.verification import Verification
from app.controllers.authentication import Authentication
from app.controllers.access_climbing_post import AccessClimbingPost

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

## User Identity Types ##
@app.route('/user/identity-type')
def identitytypelistapi():
    return UserIdentityTypes(request).get_list()

@app.route('/user/identity-type/<value>')
def identitytypedetailapi(value):
    if value.isnumeric():
        return UserIdentityTypes(request).get_detail('id', value)

    return UserIdentityTypes(request).get_detail('name', value)

@app.route('/user/identity-type', methods=['POST'])
def identitytypecreateapi():
    return UserIdentityTypes(request).create_data()

@app.route('/user/identity-type/<id>', methods=['PUT'])
def identitytypeupdateapi(id):
    return UserIdentityTypes(request).update_data(id)

@app.route('/user/identity-type/<id>', methods=['DELETE'])
def identitytypedeleteapi(id):
    return UserIdentityTypes(request).delete_data(id)
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

## Access Climbing Post ##
@app.route('/climbing-post/access')
def accessclimbingpostlistapi():
    return AccessClimbingPost(request).get_list()

@app.route('/climbing-post/access/<key>')
def accessclimbingpostdetailapi(key):
    return AccessClimbingPost(request).get_detail('key_access', key)

@app.route('/climbing-post/access', methods=['POST'])
def accessclimbingpostcreateapi():
    return AccessClimbingPost(request).create_data()

@app.route('/climbing-post/access/<key>', methods=['PUT'])
def accessclimbingpostupdateapi(key):
    return AccessClimbingPost(request).update_data(key)

@app.route('/climbing-post/access/<key>', methods=['DELETE'])
def accessclimbingpostdeleteapi(key):
    return AccessClimbingPost(request).delete_data(key)
##################

## User Types ##
@app.route('/user/type')
def typelistapi():
    return UserTypes(request).get_list()

@app.route('/user/type/<value>')
def typedetailapi(value):
    if value.isnumeric():
        return UserTypes(request).get_detail('id', value)

    return UserTypes(request).get_detail('name', value)

@app.route('/user/type', methods=['POST'])
def typecreateapi():
    return UserTypes(request).create_data()

@app.route('/user/type/<id>', methods=['PUT'])
def typeupdateapi(id):
    return UserTypes(request).update_data(id)

@app.route('/user/type/<id>', methods=['DELETE'])
def typedeleteapi(id):
    return UserTypes(request).delete_data(id)
##################

## Users ##
@app.route('/user')
def userslistapi():
    return Users(request).get_list()

@app.route('/user/<value>')
def usersdetailapi(value):
    if value.isnumeric():
        return Users(request).get_detail('id', value)

    return Users(request).get_detail('username', value)

@app.route('/user', methods=['POST'])
def userscreateapi():
    return Users(request).create_data()

@app.route('/user/<id>', methods=['PUT'])
def usersupdateapi(id):
    return Users(request).update_data(id)

@app.route('/user/<id>', methods=['DELETE'])
def usersdeleteapi(id):
    return Users(request).delete_data(id)
##################

## Verification User ##
@app.route('/verification/<token>')
def verificationapi(token):
    return Verification(request).verify(token)

@app.route('/verification/new', methods=['POST'])
def verificationnewapi():
    return Verification(request).request_new_token()
##################

## Authentication ##
@app.route('/auth/signin', methods=['POST'])
def signinapi():
    return Authentication(request).signin()

@app.route('/auth/signup', methods=['POST'])
def signupapi():
    return Authentication(request).create_data()

@app.route('/auth/signout', methods=['POST'])
def signoutapi():
    return Authentication(request).signout()

@app.route('/auth/whoami/<token>', methods=['POST'])
def whoamiapi(token):
    return Authentication(request).whoami(token)

@app.route('/auth/reset-password/<token>')
def resetpasswordcheckapi(token):
    return Authentication(request).reset_password_check(token)

@app.route('/auth/reset-password/<token>', methods=['POST'])
def resetpasswordapi(token):
    return Authentication(request).reset_password(token)

@app.route('/auth/reset-password/new', methods=['POST'])
def resetpasswordnewapi():
    return Authentication(request).request_reset_password()
##################