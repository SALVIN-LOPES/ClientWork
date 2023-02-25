from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated

from rest_framework import status

from django.http import HttpResponse

@api_view(['POST'])
def registerPage(request):
    data = request.data

    content = {'detail' : 'User created successfully'}

    return Response(content, statue = status.HTTP_200_OK)







