import os
import logging
from datetime import datetime

_logger = logging.getLogger(__name__)


def load_args(*args):
    log_path, cred_path = "kpam.log", False
    for arg in args:
        if str(arg).startswith("--log="):
            log_path = str(arg).replace("--log=", "")
        elif str(arg).startswith("--cred="):
            cred_path = str(arg).replace("--cred=", "")
    if not cred_path:
        raise Exception("Please set private key path with '--cred=private_key_path' before starting this module.")
    print(f"Log location: {log_path}")
    print(f"Private key location: {cred_path}")
    return log_path, cred_path


def validate_required_fields(**kwargs):
    required_fields = kwargs["required_fields"]
    data = kwargs["data"]
    return set(required_fields).issubset(set(data.keys()))


def validate_selection_fields(**kwargs):
    selection_fields = kwargs["selection_fields"]
    keys = kwargs["data"].keys()
    return True if set(selection_fields).intersection(set(keys)) else False


def get_app_id(filepath):
    try:
        filename = os.path.split(filepath)[-1]
        return filename.split("_")[0].lower()
    except Exception as e:
        _logger.error(f"Cannot get app id from filename: {filepath}")
        return False


def validate_datetime(time_string, fmt):
    try:
        dt = datetime.strptime(time_string, fmt)
        return True
    except Exception as e:
        _logger.error(f"Wrong Datetime format: datetime: {time_string} | format: {fmt}")
        return False
