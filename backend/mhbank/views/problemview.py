from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from mhbank.models import Problem
from mhbank.serializers import *
from django.db import connection


@api_view(['GET', 'POST'])
def problemview(request):
    if request.method == 'GET':
        data = Problem.objects.raw("select * from mhbank_problem")
        serializer = ProblemSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        pid = request.data['pid']
        name = request.data['name']
        state = 'w'
        score = 0
        text = request.data['text']
        minaar = request.data['minaar']
        maxaar = request.data['maxaar']
        level = request.data['level']
        tname = request.data['tname']
        with connection.cursor() as cursor:
            cursor.execute("insert into mhbank_problem values(%s, %s, %s, 0, %s, null, null, null, %s, %s, %s, null, null, null, null, null, null, %s)",\
             [pid, name, state, text, level, minaar, maxaar, tname])
        
        instance = Problem.objects.raw("select * from mhbank_problem where pid = %s", [pid])[0]
        serializer = ProblemSerializer(instance, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)