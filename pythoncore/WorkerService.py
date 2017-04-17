import json

from AWS import AWSClient
from Utils import get_instance_id

SFNClient = AWSClient.get_client('stepfunctions')


def start(activity_arn, task_handler):
    while True:
        # Poll for new tasks for this Activity
        task = SFNClient.get_activity_task(
            activityArn=activity_arn,
            workerName=get_instance_id()
        )

        # Parse input
        task_input = json.loads(task["input"])

        # Call handler
        task_handler(task_input, task["taskToken"])
