from django.shortcuts import render
from .models import Book
from .serailizer import BookSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import generics
from .pagination import BookPagination
from rest_framework.response import Response
from django.http import Http404
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .permission import IsOwnerPermission


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]



class BookGetList(APIView):
    def get_object(self, id):
        try:
            return Book.objects.get(id=id)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, id):
        Book = self.get_object(id)
        serailizer_class = BookSerializer(Book)
        return Response(serailizer_class.data)


class BookSearchList(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        author = self.kwargs['author']
        return Book.objects.filter(author=author)


class PermissionView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JSONWebTokenAuthentication]

    def jwt_response_payload_handler(token, user=None, request=None):
        return {
            'token': token,
            'user': BookSerializer(user, context={'request': request}).data
        }
