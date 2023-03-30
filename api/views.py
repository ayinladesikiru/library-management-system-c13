from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from book.models import Book, Author, BookInstance
from .pagination import DefaultPageNumberPagination
from .permissions import IsAdminOrReadOnly
from .serializers import BookSerializer, BookCreateSerializer, AuthorSerializer, \
    BookDetailSerializer, BookInstanceSerializer
from rest_framework import generics, status


# Create your views here.

class AuthorViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPageNumberPagination

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookInstanceViewSet(ModelViewSet):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer


class BookAuthorView(generics.ListAPIView):
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPageNumberPagination

    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer


@api_view()
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)
