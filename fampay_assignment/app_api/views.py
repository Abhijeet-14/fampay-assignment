import inspect

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from common.common_function import custom_logger, get_func_name
logger = custom_logger(__name__)

# Create your views here.
class Test(APIView):
    def get(self, request):
        func_name = get_func_name(inspect.currentframe())

        logger.info(f"Entering {func_name}: GET call for Test API")
        return Response({"result": "Test_API"}, status=status.HTTP_200_OK)
