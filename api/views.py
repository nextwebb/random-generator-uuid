from django.shortcuts import render
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from .models import Random_UUID
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
# import jwt
import os
from .serializers import UserRegistrationSerializers
from rest_framework.authentication import TokenAuthentication
# from decouple import config


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    versions = ['v1']

    def list(self, request, version="v1", *args, **kwargs):
        if version in self.versions:
            if request.user:
                try:

                    # print(response.json())
                    response = {
                        'message': Response.json()}
                    return Response(response, status=status.HTTP_200_OK)
                except IndexError:
                    response = {
                        'message': f' Hi 👋 {user.username}, some errors occured 😔.'}
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)
            else:
                response = {'message': 'API version not identified!'}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

            return Response(response, status=status.HTTP_400_BAD_REQUEST)
