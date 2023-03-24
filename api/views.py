from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from book.models import Book, Author
from .serializers import BookSerializer, BookCreateSerializer, AuthorSerializer
from rest_framework import generics


# Create your views here.

class BookCreateApiView(generics.ListAPIView):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer
