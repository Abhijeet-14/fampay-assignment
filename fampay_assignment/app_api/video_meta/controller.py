

import inspect

from rest_framework.response import Response
from rest_framework import status

from common.common_function import custom_logger, get_func_name
from exceptions.CustomExceptions import formattedException

from .service import add_youtube_video, get_youtube_video_list

logger = custom_logger(__name__)

def get_youtube_video_list_controller(request):
    """Get List of all video meta data stored in DB"""
    func_name = get_func_name(inspect.currentframe())
    try:
        logger.info(f"Enter : {func_name}")

        result = get_youtube_video_list(request)

        logger.info(f"Exit : {func_name}")

        return Response({
                    "result": result,
                    "isTrue": True
                }, 
                status=status.HTTP_200_OK
            )

    except Exception as err:
        return formattedException(err, {"isTrue": False}, func_name)


def search_video_by_title_or_description_controller(request):
    """add video's meta data to DB"""
    func_name = get_func_name(inspect.currentframe())
    try:
        logger.info(f"Enter : {func_name}")

        result = search_video_by_title_or_description(request)

        logger.info(f"Exit : {func_name}")

        return Response({
                "result": result,
                "isTrue": True
            }, 
            status=status.HTTP_200_OK
        )
    except Exception as err:
        return formattedException(err, {"isTrue": False}, func_name)
        
def add_youtube_video_controller(request):
    """add video's meta data to DB"""
    func_name = get_func_name(inspect.currentframe())
    try:
        logger.info(f"Enter : {func_name}")

        result = add_youtube_video()

        logger.info(f"Exit : {func_name}")

        return Response({
                    "result": result,
                    "isTrue": True
                }, 
                status=status.HTTP_200_OK
            )
    except Exception as err:
        return formattedException(err, {"isTrue": False}, func_name)
