from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class Test(APIView):
    def get(self, request):
        return Response({"result": "Test_API"}, status=status.HTTP_200_OK)
