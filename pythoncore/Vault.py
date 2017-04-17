from AWS import AWSClient

# Create the SSM Client
ssm = AWSClient.get_client('ssm')


def get_key(key_name):
    """
    This function reads a secure parameter from AWS' SSM service.
    The request must be passed a valid parameter name, as well as
    temporary credentials which can be used to access the parameter.
    The parameter's value is returned.
    """

    # Get the requested parameter
    response = ssm.get_parameters(
        Names=[
            key_name,
        ],
        WithDecryption=True
    )

    # Store the credentials in a variable
    key = response['Parameters'][0]['Value']

    return key
