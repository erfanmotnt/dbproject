from django.contrib.auth.models import User
from rest_framework import serializers
from mhbank.models import *
from django.db import transaction
from django.utils import timezone


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

