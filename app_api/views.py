from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import AuthorSerializer, BookSerializer
from app_bookstore.models import Author, Book
from app_users.models import CustomUser


User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def apiRoutes(request):
    routes = {
        'Authors': 'api/authors/',
        'Author': 'api/author/<int:pk>/',
        'Books': 'api/books/',
    }
    return Response(routes)


@api_view(['GET', 'POST'])
def apiAuthors(request):
    if request.method == 'GET':
        qs = Author.objects.all()
        serializer = AuthorSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_created=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def apiAuthor(request, pk):
    try:
        qs = Author.objects.get(id=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AuthorSerializer(qs, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = AuthorSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save(user_created=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        


@api_view(['GET'])
def apiBooks(request):
    try:
        qs = Book.objects.all()
        serializer = BookSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except PermissionError:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    except (ConnectionAbortedError, ConnectionError, ConnectionRefusedError, ConnectionResetError):
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
