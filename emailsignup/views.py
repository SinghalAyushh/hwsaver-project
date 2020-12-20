from django.shortcuts import render


from rest_framework.decorators import api_view

@api_view()
def null_view(request):
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view()
def complete_view(request):
    return Response("Email account is activated",status=status.HTTP_200_OK)

from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response

from knox.models import AuthToken
from .serializers import (
                          UserSerializer, LoginUserSerializer)
       

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data
        return Response({
            "userid": UserSerializer(email, context=self.get_serializer_context()).data,
            "login_type": "signin"
        })
        