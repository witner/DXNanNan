from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class TPrioritySerializer(serializers.Serializer):
    dimension_id = serializers.IntegerField(read_only=True)
    select = serializers.ChoiceField()
