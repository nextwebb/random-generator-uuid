from django.shortcuts import render
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from .models import Random_UUID
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
# import jwt
import os
from .serializers import UUIDSerializers
from rest_framework.authentication import TokenAuthentication
# from decouple import config
import uuid


class UUIDViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UUIDSerializers
    permission_classes = (AllowAny,)
    versions = ['v1']

    def list(self, request, version="v1", *args, **kwargs):
        if version in self.versions:
            if request.user:
                try:
                    uuid.uuid4()
                    uuid_string = str(uuid.uuid4())
                    print(uuid_string)

                    # random_UUID_instance = Random_UUID(uuid=uuid_string)
                    # random_UUID_instance.save()
                    all_uuid_objects = Random_UUID.objects.all()

                    serializer = UUIDSerializers(all_uuid_objects, many=True)
                    data = serializer.data[:]
                    # print(len(data))

                    for index, item in range(len(data)):
                        for key in data[index]:
                            print(data[index][key])

                    response = {'message': 'Hi 👋 WORKING!',
                                'result': serializer.data}

                    # print(type(serializer.data.keys))
                    return Response(response, status=status.HTTP_200_OK)
                except IndexError:
                    response = {
                        'message': ' Hi 👋 error}'}
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)
            else:
                response = {'message': 'API version not identified!'}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = {
                'message': 'inavlid api version'}

            return Response(response, status=status.HTTP_400_BAD_REQUEST)
