from asyncio.log import logger
from functools import partial
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EmployeeSerializers, SignupSerializers
from .models import Employee
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
import logging
from project1.settings import LOGGING

logging = logging.getLogger('django')
print(__name__)


class EmployeeApiView(APIView):

    def post(self, request):

        serializer = EmployeeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logging.info('Posting Data')
            return Response(data=serializer.data, status=201)
        logging.info(
            'Data is Not Valid>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        return Response(data=serializer.errors, status=400)

    def get(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializers(queryset, many=True)
        logging.info('Getting All Data')
        return Response(data=serializer.data, status=200)


class EmployeeDetails(APIView):

    def get(self, request, pk=None):
        try:
            queryset = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializers(queryset)
            return Response(data=serializer.data, status=200)
        except:
            return Response(data={'message': 'Not Found'}, status=400)

    def delete(self, request, pk=None):
        try:
            queryset = Employee.objects.get(pk=pk)
            queryset.delete()
            return Response(data={'message': 'Deleted'}, status=204)
        except:
            return Response(data={'message': 'Not Found'}, status=400)

    def put(self, request, pk=None):
        try:
            queryset = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializers(
                data=request.data, instance=queryset, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=205)
            return Response(data=serializer.errors, status=400)
        except:
            return Response(data={'message': 'Not Found'}, status=400)

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class SignupAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializers
