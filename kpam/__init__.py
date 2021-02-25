from flask import Blueprint, current_app
import logging
from config import Config
import sys

kpam_logger = logging.getLogger("KPAM")
consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setLevel(logging.INFO)
kpam_logger.addHandler(consoleHandler)

kpam_bp = Blueprint("kpam", __name__)

# verfiy that all needed config is in config file
required_configs = ['PRIVATE_KEY','APP_ID'] 

if not all(required_config in vars(Config) for required_config in required_configs):
    error_str = "Not all required config for kpam is provide in enviroment variable please checked\n"
    error_str =  error_str + "required config:{}".format(required_configs)
    raise Exception(error_str) 

from kpam.kpam import *


