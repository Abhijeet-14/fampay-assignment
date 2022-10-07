import json
import os
import requests
import inspect

from rest_framework import status

from app_api import constants
from common.common_function import custom_logger, get_func_name
from exceptions.CustomExceptions import CustomApiException


from .models import YouTubeVideo
from .serializer import GetYouTubeVideoSerializer, YouTubeVideoModelSerializer

logger = custom_logger(__name__)

def get_youtube_video_list(request):
    """Get All video meta_data list in descending order of published_at"""
    func_name = get_func_name(inspect.currentframe())
    try:
        logger.info(f"Enter : {func_name}")

        request_serializer = GetYouTubeVideoSerializer(data=request.GET)
        serializer_name = "Get YouTube Video Data from DB"

        if not request_serializer.is_valid():
            logger.error(f"{serializer_name} :: Serializer error :: {request_serializer.errors}")

            raise CustomApiException(
                f"Inputs value are invalid or few input fields are missing :: {list(request_serializer.errors.keys())}",
                status.HTTP_400_BAD_REQUEST
            )
            
        validate_data = dict(request_serializer.validated_data)

        offset = validate_data['offset']
        limit = validate_data['limit']

        logger.info(f"Query all YouTubeVideo instance with offset {offset} :: limit {limit}")

        # offset + limit : [10:10] will give [] result
        # so, offset + limit : [10: 10 + 10] will give next 10 result starting from 11.
        all_video_meta = YouTubeVideo.objects.all()[offset: offset + limit] 

        # Response Serializer
        response_serializer = YouTubeVideoModelSerializer(all_video_meta, many=True)
        result = response_serializer.data

        logger.info(f"Exit : {func_name}")
        return result
    except Exception as err:
        logger.error(f"Exit : {func_name} :: Error : {str(err)}")
        raise err


def search_video_by_title_or_description(request):
    func_name = get_func_name(inspect.currentframe())
    try:
        logger.info(f"Enter : {func_name}")
    
        request_serializer = GetYouTubeVideoSerializer(data=request.GET)
        serializer_name = "Search YT Video from DB on Title and Description"

        if not request_serializer.is_valid():
            logger.error(f"{serializer_name} :: Serializer error :: {request_serializer.errors}")

            raise CustomApiException(
                f"Inputs value are invalid or few input fields are missing :: {list(request_serializer.errors.keys())}",
                status.HTTP_400_BAD_REQUEST
            )
            
        validate_data = dict(request_serializer.validated_data)

        offset = validate_data.get('offset')
        limit = validate_data.get('limit')

        title = validate_data.get('title')
        description = validate_data.get('description')

        logger.info(f"Filter Query on Video stored in DB with title {title} OR description {description} by using like command %title%")

        all_video_meta = ""

        if title is not None:
            logger.debug("Title is not None")
            all_video_meta = YouTubeVideo.objects.filter(title__contains = title) 

        if description is not None:
            logger.debug("Description is not None")
            all_video_meta += YouTubeVideo.objects.filter(description__contains = description)
        
        logger.debug("Combining the matched video with title & description & apply offset & limit")
        all_video_meta = all_video_meta[offset: offset + limit] 

        # Response Serializer
        response_serializer = YouTubeVideoModelSerializer(all_video_meta, many=True)
        result = response_serializer.data

        logger.info(f"Exit : {func_name}")
        return result
    except Exception as err:
        logger.error(f"Exit : {func_name} :: Error : {str(err)}")
        raise err



def add_youtube_video():
    func_name = get_func_name(inspect.currentframe())
    try:
        logger.info(f"Enter : {func_name}")

        logger.info("Get List of video from Youtube Data API")
        videos_meta_list_response = get_youtube_video_from_YT_Developer_API()

        bulk_insert_video_list = []
        
        for video in videos_meta_list_response:
            instance = YouTubeVideo(
                title =video.get('title'),
                description =video.get('description'),
                channel_title =video.get('channelTitle'),
                channel_id =video.get('channelId'),
                published_at =video.get('publishedAt'),
                published_time =video.get('publishTime'),
            )

            bulk_insert_video_list.append(instance)

        logger.info("Bulk creating YouTubeVideo Instance")
        bulk_create_video_list_instance = YouTubeVideo.objects.bulk_create(bulk_insert_video_list)

        response_serializer = YouTubeVideoModelSerializer(bulk_create_video_list_instance, many=True)
        result = response_serializer.data

        logger.info(f"Exit : {func_name}")
        return result
    except Exception as err:
        logger.error(f"Exit : {func_name} :: Error : {str(err)}")
        raise err

def get_youtube_video_from_YT_Developer_API():
    func_name = get_func_name(inspect.currentframe())
    try:
        logger.info(f"Enter : {func_name}")
        
        base_url = constants.BASE_URL 

        part = constants.SEARCH_PART
        type = constants.SEARCH_TYPE
        max_results = constants.SEARCH_MAX_RESULT

        api_key = os.environ.get(constants.API_KEY)
        search_query = os.environ.get(constants.SEARCH_QUERY_KEYWORD)

        url =  f"{base_url}?part={part}&type={type}&maxResults={max_results}&q={search_query}&key={api_key}"

        logger.info("Calling Youtube Data API v3 for search !")
        response = requests.get(url)

        status_code = response.status_code
        logger.info(f"status_code : {status_code}")

        if status_code != 200:
            logger.error(f"{status_code} :: {response.text}")

        result = response.json()
        logger.debug(f"No of videos: {len(result)}")

        final_result = []
        for val in result.get('items'):
            val = val.get('snippet')

            val.pop('thumbnails')
            val.pop('liveBroadcastContent')

            final_result.append(val)

        logger.info(f"Exit : {func_name} :: {len(final_result)}")
        return final_result

    except Exception as err:
        logger.error(f"Exit : {func_name} :: {str(err)}")
        raise err