import hashlib
from django.utils.translation import ugettext_noop as _
from django.contrib.auth.hashers import BasePasswordHasher, mask_hash
# from django.utils.datastructures import OrderedDict
from collections import OrderedDict
class SHA256PasswordHasher(BasePasswordHasher):
    algorithm = "sha256"
    def encode(self, password, salt, iterations=None):
        assert password is not None
        return hashlib.sha256(password.encode('utf-8')).hexdigest()
    def verify(self, password, encoded):
        return hashlib.sha256(password.encode('utf-8')).hexdigest() == encoded
    def safe_summary(self, encoded):
        algorithm, iterations, salt, hash = encoded.split('$', 3)
        return OrderedDict([
            (_('algorithm'), 'md5'),
            (_('hash'), mask_hash(hash)),
        ])