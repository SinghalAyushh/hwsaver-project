from rest_framework import serializers

from favourites.models import Fav

class FavSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Fav
        fields = '__all__'
