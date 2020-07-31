import os
import time
import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser

from django.http import HttpResponse
from django.conf import settings as conf_settings

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class QuestionnaireView(APIView):
    '''
    Questionnaire APIs 
    '''

    @swagger_auto_schema(
        manual_parameters=[],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="OK"
            )
        }
    )
    def get(self, request):
        '''
        Get all questionnaire list
        '''
        content = ""

        with open(os.path.join(conf_settings.BASE_DIR, 'data.json'), 'r') as data_file:
            content = json.load(data_file)
        return Response(content)

class SyncDataView(APIView):
    parser_classes = [MultiPartParser]

    @swagger_auto_schema(
        manual_parameters=[],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="OK"
            )
        }
    )
    def put(self, request):
        files = []
        for file_handle in request.FILES:
            file_name = request.FILES[file_handle].name

            file_data = request.FILES.getlist(file_handle)
            for f in file_data:
                with open(os.path.join(conf_settings.BASE_DIR, "uploads", file_name), 'wb') as data_file:
                    for chunk in f.chunks():
                        data_file.write(chunk)

            files.append(file_name)
        return Response(', '.join(files), status.HTTP_201_CREATED)