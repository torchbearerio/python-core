AWS_REGION = 'us-west-2'

TASK_ARNS = {
    'CV_SALIENCY': 'arn:aws:states:us-west-2:814009652816:activity:CV_SALIENCY',
    'CV_DESCRIPTION': 'arn:aws:states:us-west-2:814009652816:activity:CV_DESCRIPTION',
    'CV_GET_COLORS': 'arn:aws:states:us-west-2:814009652816:activity:CV_GET_COLORS',
    'LANDMARK_DECIDERER': 'arn:aws:states:us-west-2:814009652816:activity:LANDMARK_DECIDERER',
    'LANDMARK_MARKER': 'arn:aws:states:us-west-2:814009652816:activity:LANDMARK_MARKER',
    'CROP_FROM_CV': 'arn:aws:states:us-west-2:814009652816:activity:CROP_FROM_CV',
    'PIPELINE_FINISH': 'arn:aws:states:us-west-2:814009652816:activity:PIPELINE_FINISH',
    'CROP_FROM_TURK': 'arn:aws:states:us-west-2:814009652816:activity:CROP_FROM_TURK'
}

S3_BUCKETS = {
    'STREETVIEW_IMAGES': 'torchbearer-sv-images',
    'SALIENCY_MAPS': 'torchbearer-saliency-maps',
    'CROPPED_IMAGES': 'torchbearer-cropped-images',
    'TRANSPARENT_CROPPED_IMAGES': 'torchbearer-transparent-cropped-images',
    'MARKED_LANDMARK_IMAGES': 'torchbearer-marked-landmark-images'
}

HIT_STATUS = {
    "HIT_STATUS_PROCESSING": "PROCESSING",
    "HIT_STATUS_UNKNOWN": "UNKNOWN",
    "HIT_STATUS_COMPLETE": "COMPLETE"
}
