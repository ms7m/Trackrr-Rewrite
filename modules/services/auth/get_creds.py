# Authorization 
# Get_Creds module

import os
from loguru import logger
import importlib
import sys

"""
class AuthorizationSpecific(object):
    def __init__(self, service_name):

        self._service_name = ''.join([i for i in service_name if i.isalpha()])

        self.service_name = "services." + str(self._service_name).strip()
"""


class Authorization(object):
    def __init__(self):
        try:
            self._enc_pro = os.environ['trackrrAPI_decrypt_Key']
        except Exception as error:
            print("Failure.")
            logger.error(f"Authorization env get failed: {error}")
    @logger.catch
    def authorize_service(self, service_name):
        try:
            self._service_name = ''.join([i for i in service_name if i.isalpha()])
            self.service_name = "modules.services.auth.services_auth." + str(self._service_name).strip()
            logger.info(self.service_name)
            module_import = importlib.import_module(self.service_name)
        except Exception as error:
            logger.error(f"error on 34: {error}")
        try:
            core_import_str = str(module_import.Service.CORE)
            logger.info(core_import_str)
            core_import = importlib.import_module(core_import_str)
            logger.info(core_import.Ref)
            RefObj = core_import.Ref.main_obj
            return RefObj(module_import.Service)
        except Exception as error:
            logger.error(f"Could not create auth_verifeid: {error}")