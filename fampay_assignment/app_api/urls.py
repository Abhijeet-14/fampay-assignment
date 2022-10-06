from django.urls import path

from . import views

urlpatterns = [
    # Author
    path("test/", views.Test.as_view(), name="test-api"),
]
