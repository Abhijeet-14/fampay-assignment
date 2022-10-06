from django.urls import path

from . import views

urlpatterns = [
    # Author
    path("youtubevideos/", views.YouTubeVideoData.as_view(), name="video-meta-api"),
    path("search/", views.SearchVideo.as_view(), name="video-meta-api"),
]
