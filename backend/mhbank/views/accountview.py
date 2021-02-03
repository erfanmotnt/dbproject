from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from mhbank.models import Account
from mhbank.serializers import *
from django.db import connection

@api_view(['POST'])
def accountview(request):
    if request.method == 'POST':
        username = request.data['username']
        firstname = request.data['firstname']
        lastname = request.data['lastname']
        phone = request.data['phone']
        email = request.data['email']
        role = request.data['role']
        with connection.cursor() as cursor:
            cursor.execute("insert into mhbank_account values(%s, %s, %s, %s, %s, %s)",\
             [username, firstname, lastname, phone, email, role])

