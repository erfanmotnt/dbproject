from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from mhbank.models import Problem
from mhbank.serializers import *
from django.db import connection


@api_view(['GET'])
def initial(request):
    with connection.cursor() as cursor:
        #example
        cursor.execute("""CREATE ASSERTION  TOTCRED-CHECKCHECK 
        (NOT EXISTS (SELECT STIDFROM COTJOIN  STCOTGROUP BY  (STID, TR, YR)HAVING SUM(CREDIT) > 20) )
        """)
        
    return Response(serializer.data, status=status.HTTP_200_OK)