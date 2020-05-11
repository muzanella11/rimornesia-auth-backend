from cryptography.fernet import Fernet
import os

class Secrets(object):
    prefix_key = 'enem'
    subfix_key = 'project'
    key_secret = b'Gqtv_DlmPiGbdYU6dGA0Za-Iei1Kvs9NT_vVrv-vQx0='
    value = ''
    config = None

    def __init__(self, config = None):
        super(Secrets, self).__init__()

        self.config = config
        self.value = self.config.get('value')

    def generate_key(self):
        key = Fernet.generate_key()

        return key

    def combine_key(self, token):
        self.value = "{}//{}//{}//{}".format(self.prefix_key, self.value, self.subfix_key, token)

    def encrypt(self):
        f = Fernet(self.key_secret)
        token = f.encrypt(b"{}".format(self.value))

        return token

    def decrypt(self):
        f = Fernet(self.key_secret)
        f_text = b"{}".format(self.value)
        result = (f.decrypt(f_text))

        return result
