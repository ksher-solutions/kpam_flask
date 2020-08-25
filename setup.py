from setuptools import setup, find_packages

setup(
    name='kpam',
    version='0.0.1',
    packages=find_packages(include=['kpam', 'kpam.*']),
    install_requires=[
        'rsa',
        'flask',
        'requests'
    ]
)