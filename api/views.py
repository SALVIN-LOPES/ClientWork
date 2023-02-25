from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from django.contrib.auth.models import User
from api.serializers import UserSerializer, WorkSerializer,ArtistSerializer
from api.models import Artist,Work,Client


from rest_framework import status

from django.http import HttpResponse

@api_view(['POST'])
def registerPage(request):
    data = request.data
    try:
        user = User.objects.create(
                username = data['username'],
                email = data['email'],
                password = data['password']
            )
        serializer = UserSerializer(user,many=False)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except:
        message = {'detail' : 'User with this email alredy exist' }
        return Response(message,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getWorks(request):
    
    query = request.GET
    # URL = http://127.0.0.1:8000

    # get all the works
    # url = {{URL}}/api/works/
    if len(query) == 0:
        works =  Work.objects.all()
        if works and len(works) > 0:
            serializer = WorkSerializer(works,many=True)
            message = {'detail' : 'Works','content' : serializer.data}
            return Response(message,status=status.HTTP_200_OK)
        else:
            message = {'detail' : 'There are no works'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
    
    # get the work by artist name
    # url = {{URL}}/api/works?artist=[artist name]
    elif(len(query) > 0 and query.get('artist')):
        # find the work with the artist name
        works =  Work.objects.filter(artist__name__icontains=query.get('artist'))
        if works : 
            serializer = WorkSerializer(works,many=True)
            message = {'detail' : 'Works','content' : serializer.data}
            return Response(message,status=status.HTTP_200_OK)
        else:
            message = {'detail' : 'There are no works for artist name'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)

    # get the artist by work_type
    # url = {{URL}}/api/works?work_type=[work_type]
    else:
        # work_type = pk | pk = Youtube, Instagram, Other
        # find the artists with the work_type
        artists =  Artist.objects.filter(work__work_type__icontains = query.get('work_type'))
        if artists:
            serializer = ArtistSerializer(artists,many=True)
            message = {'detail' : 'Artists','content' : serializer.data}
            return Response(message,status=status.HTTP_200_OK)
        else:
            message = {'detail' : 'There are no Artists for artist name'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)









