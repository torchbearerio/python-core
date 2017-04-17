import boto3
import os
from ..Constants import AWS_REGION
from ..Utils import is_dev

# Create the SSM Client
__session = boto3.Session(profile_name='torchbearer') if is_dev() else boto3.Session()


def get_client(service):
    return __session.client(service, region_name=AWS_REGION)
