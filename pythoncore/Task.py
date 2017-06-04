import json

from AWS import AWSClient


class Task (object):
    task_token = None
    ep_id = None
    hit_id = None

    def __init__(self, _ep_id, _hit_id, _task_token):
        self.task_token = _task_token
        self.ep_id = _ep_id
        self.hit_id = _hit_id

    def send_success(self):
        client = AWSClient.get_client('stepfunctions')
        client.send_task_success(
            taskToken=self.task_token,
            output=json.dumps({'epId': self.ep_id, 'hitId': self.hit_id})
        )

    def send_failure(self, err_code, err_message):
        client = AWSClient.get_client('stepfunctions')
        client.send_task_failure(
            taskToken=self.task_token,
            error=err_code,
            cause=err_message
        )

    def run(self):
        pass

