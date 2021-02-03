from django.contrib.auth.models import User
from rest_framework import serializers
from mhbank.models import *
from django.db import transaction
from django.utils import timezone


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class SubTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'



class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
