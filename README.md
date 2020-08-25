# kpam
Ksher Payment Agent Module

## Introduction

KPAM is a Python module, it's an agent for Ksher Payment Services, with below features:

- Exposing simple API for application to use
- Handling the connection setup and communication encryption/protection with Ksher Services
- Logging for all the payment related information, but without the sensitive information which should not be logged

## How to install

```
pip install kpam
```

## How to use

Private key must include merchant id as a filename.

For testing

```
python -m kpam --log=absolute_path_to_log_file --cred=absolute_path_to_private_key
```

Example
```
python -m kpam --log=/var/log/kpam.log --cred=/var/credentials/Mch12345_PrivateKey.pem
```

For production, it's recommended to run the above under supervisor.

## API


## Test Drive



