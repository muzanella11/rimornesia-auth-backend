from app.core.secrets import Secrets
from app.libraries.token_handler import TokenHandler
import re

class Helpers(object):
    def __init__(self):
        super(Helpers, self).__init__()

    def is_email(self, email):
        return bool(email.find('@') != -1)

    def email_validator(self, email):
        return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

    def encrypt(self, value):
        return Secrets({
            'value': value
        }).encrypt()

    def decrypt(self, value):
        return Secrets({
            'value': value
        }).decrypt()

    def check_expired(self, expired_time = None):
        return TokenHandler().check_expired_time(expired_time)