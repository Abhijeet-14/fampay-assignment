import inspect

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from common.common_function import custom_logger, get_func_name
from exceptions.CustomExceptions import formattedException

logger = custom_logger(__name__)

# Create your views here.
class Test(APIView):
    def get(self, request):
        func_name = get_func_name(inspect.currentframe())
        try:
            logger.info(f"Entering {func_name}: GET call for Test API")
            
            div = 1/0

            return Response({"result": "Test_API"}, status=status.HTTP_200_OK)
        except Exception as err:
            return formattedException(err, {"isTrue": False}, func_name)
