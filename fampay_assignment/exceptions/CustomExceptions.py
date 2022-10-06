import logging

from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler

import inspect
from common.common_function import custom_logger, get_func_name
logger = custom_logger(__name__)


class CustomApiException(APIException):
    """Custom Exceptopms to raise as per our need"""

    # public fields
    detail = None
    status_code = None

    # constructor
    def __init__(self, message, status_code):
        # override public fields
        CustomApiException.detail = message
        CustomApiException.status_code = status_code


def custom_exception_handler(exec, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exec, context)

    if response is not None:
        response.data["status_code"] = response.status_code

        response.data["message"] = response.data["detail"]

        # del response.data["detail"]

    return response


def formattedException(error, others=None, func_name=""):
    """
    Exception format for an api
    error: error message
    others: extra key-value item as dict
    """

    logger.error(f"{func_name} {str(error)}")
    try:
        status_code = error.status_code
    except Exception:
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    message = {"error": str(error)}
    if others is not None:
        message.update(others)

    return Response(message, status=status_code)
