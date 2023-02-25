from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Artist, Work, Client

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = '__all__'

class WorkSerializer(serializers.ModelSerializer):
    class Meta :
        model = Work
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):

    class Meta :
        model = Artist
        fields = '__all__'
    
