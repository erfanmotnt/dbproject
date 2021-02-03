from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from mhbank.models import Tag
from mhbank.serializers import *


@api_view(['GET'])
def tagview(request):
    data = Tag.objects.raw("select * from mhbank_tag")
    serializer = TagSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def subtagview(request):
    data = SubTag.objects.raw("select * from mhbank_subtag")
    serializer = SubTagSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)