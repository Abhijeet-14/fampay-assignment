from django.db import models

from common.common_function import custom_logger
logger = custom_logger(__name__)

class YouTubeVideo(models.Model):
    id = models.BigAutoField(
        primary_key=True, auto_created=True, serialize=False
    )

    title = models.CharField(max_length=120)
    description = models.CharField(max_length=300)
    
    channel_title = models.CharField(max_length=120)
    channel_id = models.CharField(max_length=120)

    published_at = models.DateTimeField() 
    published_time = models.DateTimeField() 

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title[0:50] + " ..."