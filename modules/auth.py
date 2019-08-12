

# Broken don't use


import json
import datetime
import os
from .exceptions import AuthorizationPathFailure, AuthorizationIncorrectFormat, AuthorizationParseError


class Authorization(object):
    def __init__(self, auth_dict):
        self.auth_dict = auth_dict
        if isinstance(self.auth_dict, AuthorizationGrabber) != True:
            raise AuthorizationIncorrectFormat(f"{type(self.auth_dict)} was recieved instead of a dict.")
        else:
            pass

            
class AuthorizationGrabber(object):
    def __init__(self, authorization_type):
        # Auth types
        # 1 - JSON File
        # 2 - OS environments

        self.authorization_type = int(authorization_type)

        if self.authorization_type == 1:
            OS_KEY_PATH = os.environ("TRACKRR_KEY_PATH")
            try:
                self.auth_file = json.load(open(OS_KEY_PATH, 'r'))
            except Exception as error:
                AuthorizationParseError(error)
    @property
    def to_dict():
        return self.auth_file

