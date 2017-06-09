import boto3
import botocore
import sys
from botocore.client import Config
from botocore.session import Session
from ..Constants import AWS_REGION
from ..Utils import is_dev
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--AWS_SECRET")
parser.add_argument("--AWS_ACCESS_KEY")
args = parser.parse_args()

# Create the SSM Client
if args.AWS_SECRET and args.AWS_ACCESS_KEY:
    __session = boto3.Session(aws_secret_access_key=args.AWS_SECRET, aws_access_key_id=args.AWS_ACCESS_KEY)
else:
    __session = boto3.Session(profile_name='torchbearer') if is_dev() else boto3.Session()

__s3_resource = __session.resource('s3')


def get_client(service):
    read_timeout = 70 if service == 'stepfunctions' else 60
    config = Config(connect_timeout=50, read_timeout=read_timeout)

    return __session.client(service, region_name=AWS_REGION, config=config)


def s3_key_exists(bucket, key):
    exists = False

    try:
        __s3_resource.Object(bucket, key).load()
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            exists = False
        else:
            raise
    else:
        exists = True

    return exists
