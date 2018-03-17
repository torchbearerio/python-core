import json
from multiprocessing import Pool
import traceback
from AWS import AWSClient
from Utils import get_instance_id

SFNClient = AWSClient.get_client('stepfunctions')

def _task_generator(tasks):
    for t in tasks:
        for w in range(_num_workers(t)):
            yield t

def _num_workers(task):
    return task[2] if len(task) > 2 else 1

def start(*tasks_tuple):
    num_workers = reduce(lambda sum, t: sum + _num_workers(t), tasks_tuple, 0)

    # We now have a list of each jobs repeated num_workers times.
    # Get them sent out to the worker pool
    print("Starting WorkerService for {tasks} tasks with {workers} total workers"
         .format(tasks=len(tasks_tuple), workers=num_workers))
    pool = Pool(processes=num_workers)
    pool.map(_run_task, _task_generator(tasks_tuple))


def _run_task(task_tuple):
    activity_arn = task_tuple[0]
    task_handler = task_tuple[1]

    while True:
        # Poll for new tasks for this Activity
        task = SFNClient.get_activity_task(
            activityArn=activity_arn,
            workerName=get_instance_id()
        )

        if not task.get("input"):
            continue

        # Parse input
        task_input = json.loads(task["input"])

        # Call handler
        try:
            task_handler(task_input, task["taskToken"])
        except Exception as ex:
            print ("Error running task handler for " + activity_arn)
            traceback.print_exc()
