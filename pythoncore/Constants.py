AWS_REGION = 'us-west-2'

TASK_ARNS = {
    'CV_GET_SALIENCY_MASK': 'arn:aws:states:us-west-2:814009652816:activity:CV_GET_SALIENCY_MASK'
}

S3_BUCKETS = {
    'STREETVIEW_IMAGES':            'torchbearer-sv-images',
    'SALIENCY_MAPS':                'torchbearer-saliency-maps',
    'CROPPED_IMAGES':               'torchbearer-cropped-images',
    'TRANSPARENT_CROPPED_IMAGES':   'torchbearer-transparent-cropped-images'
}