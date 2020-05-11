from flask import request
from app import app
from app.controllers.health_indicator import HealthIndicator
from app.controllers.secret import Secret

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