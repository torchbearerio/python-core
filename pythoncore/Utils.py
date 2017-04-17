import requests
import os


def is_dev():
    return 'DEV' in os.environ


def get_instance_id():
    if is_dev():
        return 'Dev Machine'

    response = requests.get('http://169.254.169.254/latest/meta-data/instance-id')
    return response.text
