import sys
import logging
from kpam.kpam import start_server
from kpam.utils import load_args

if __name__ == "__main__":
    log_path, private_key_path = load_args(*sys.argv)
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(filename=log_path, level=logging.INFO, format=log_fmt)
    start_server(env="dev", debug=True, cred_key=private_key_path)
