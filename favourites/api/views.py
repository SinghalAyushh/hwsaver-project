from django.contrib.auth import get_user_model
from rest_framework import permissions,viewsets

from favourites.models import Fav

from .serializers import *




class FavView(viewsets.ModelViewSet):
    queryset = Fav.objects.all()
    serializer_class = FavSerializer
    permission_classes = (permissions.AllowAny, )    
