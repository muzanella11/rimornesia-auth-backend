from cryptography.fernet import Fernet
import os

class Secrets(object):
    prefix_key = 'enem'
    subfix_key = 'project'
    key_secret = 'Gqtv_DlmPiGbdYU6dGA0Za-Iei1Kvs9NT_vVrv-vQx0='
    value = ''
    config = None

    def __init__(self, config = None):
        super(Secrets, self).__init__()

        self.config = config
        self.value = self.config.get('value')

    def generate_key(self):
        key = Fernet.generate_key()
        key = key.decode('utf-8')

        return key

    def combine_key(self, token):
        self.value = "{}//{}//{}//{}".format(self.prefix_key, self.value, self.subfix_key, token)

    def encrypt(self):
        f = Fernet(self.key_secret)
        token = f.encrypt('{}'.format(self.value).encode())
        token = token.decode('utf-8')

        return token

    def decrypt(self):
        f = Fernet(self.key_secret)
        f_text = "{}".format(self.value).encode()
        result = (f.decrypt(f_text))
        result = result.decode('utf-8')

        return result
