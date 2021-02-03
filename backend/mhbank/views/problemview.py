from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from mhbank.models import Problem
from mhbank.serializers import *


@api_view(['GET'])
def problemview(request):
    if request.method == 'GET':
        data = Problem.objects.raw("select * from mhbank_problem")
        serializer = ProblemSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = FilterSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        data = serializer.validated_data

    q_list = getQuestionsByRemovePermitions(request, getQuestionsByFilter(**data))
    from django.conf import settings