from rest_framework.serializers import ModelSerializer

from .models import *


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'