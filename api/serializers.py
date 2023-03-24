from rest_framework import serializers
from book.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('title', 'description', 'author')


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'isbn', 'description')
