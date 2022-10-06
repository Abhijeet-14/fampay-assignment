import inspect

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from common.common_function import custom_logger
from app_api.video_meta.controller import add_youtube_video_controller, get_youtube_video_list_controller

logger = custom_logger(__name__)

# Create your views here.
class YouTubeVideoData(APIView):
    def get(self, request):
        return get_youtube_video_list_controller(request)

    def post(self, request):
        return add_youtube_video_controller(request)
