import boto3
from botocore.client import Config
from botocore.session import Session
from ..Constants import AWS_REGION
from ..Utils import is_dev

# Create the SSM Client
__session = boto3.Session(profile_name='torchbearer') if is_dev() else boto3.Session()


def get_client(service):
    read_timeout = 70 if service == 'stepfunctions' else 60
    config = Config(connect_timeout=50, read_timeout=read_timeout)

    return __session.client(service, region_name=AWS_REGION, config=config)
