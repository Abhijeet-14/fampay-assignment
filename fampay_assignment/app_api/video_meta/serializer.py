from email.policy import default
from rest_framework import serializers

from app_api.video_meta.models import YouTubeVideo


class GetYouTubeVideoSerializer(serializers.Serializer):
    limit = serializers.IntegerField(required=False, default=25)
    offset = serializers.IntegerField(required=False, default=0)

class YouTubeVideoModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = YouTubeVideo
        fields = "__all__"
