from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    print(response)
    # Now add the HTTP status code to the response.
    if response.status_code == 404:
        response.data['status_code'] = 555
        response.data['detail'] = 'Testing...'
    elif response is not None:
        response.data['status_code'] = response.status_code
    return response
