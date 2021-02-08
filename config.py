import os

class Config:
    """Config value will be obtaion from environment variable and stored here
    to be use later in flask application.
    """
    APP_ID = os.environ["APP_ID"]
    PRIVATE_KEY = os.environ["PRIVATE_KEY"]
    # OMISE_SECRET_KEY = os.environ["OMISE_SECRET_KEY"]
    # OMISE_PUBLIC_KEY = os.environ["OMISE_PUBLIC_KEY"]
    # SECRET_KEY = os.environ["FLASK_SECRET_KEY"]
    # OMISE_API_VERSION = os.environ.get("OMISE_API_VERSION", "2019-05-29")
    # OMISE_API_BASE = os.environ.get("OMISE_API_BASE", "https://api.omise.co")
    # STORE_LOCALE = os.environ.get("STORE_LOCALE", "th_TH")
    # STORE_CURRENCY = os.environ.get("STORE_CURRENCY", "THB")
    # PREFERRED_URL_SCHEME = os.environ.get("PREFERRED_URL_SCHEME", "https")
    # SERVER_NAME = os.environ.get("SERVER_NAME")
    # # AUTO_CAPTURE defaults to True unless set to 0, false, or False
    # AUTO_CAPTURE = os.environ.get("AUTO_CAPTURE") not in [0, "false", "False"]
    # # LOCATION defaults to True unless set to 0, false, or False
    # LOCATION = os.environ.get("LOCATION") not in [0, "false", "False"]