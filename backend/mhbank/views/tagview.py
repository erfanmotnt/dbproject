from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from mhbank.models import Tag
from mhbank.serializers import *
from django.db import connection

@api_view(['GET', 'POST'])
def tagview(request):
    if request.method == 'GET':
        data = Tag.objects.raw("select * from mhbank_tag")
        serializer = TagSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        tname = request.data['tname']
        cusername = request.data['cusername']
        with connection.cursor() as cursor:
            cursor.execute("insert into mhbank_tag values(%s, %s)", [tname, cusername])
        
        instance = Tag.objects.raw("select * from mhbank_tag where tname = %s", [tname])[0]
        serializer = TagSerializer(instance, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def subtagview(request):
    if request.method == 'GET':
        data = SubTag.objects.raw("select * from mhbank_subtag")
        serializer = SubTagSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        tname = request.data['tname']
        stname = request.data['stname']
        stid = hash(tname+stname)%1000
        cusername = request.data['cusername']
        with connection.cursor() as cursor:
            cursor.execute("insert into mhbank_subtag values(%s, %s, null, null, %s)", [stid, stname, tname])
        
        instance = SubTag.objects.raw("select * from mhbank_subtag where stid = %s", [stid])[0]
        serializer = SubTagSerializer(instance, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)