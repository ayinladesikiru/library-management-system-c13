from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from book.models import Book, Author, BookInstance


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'date_of_birth']

    date_of_birth = serializers.DateTimeField(read_only=True)


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('title', 'description', 'price', 'date_added', 'discount_price', 'author')

    author = serializers.HyperlinkedRelatedField(
        queryset=Author.objects.all(),
        view_name='author-detail',
    )
    date_added = serializers.DateTimeField(read_only=True)
    discount_price = serializers.SerializerMethodField(method_name='discount')

    def discount(self, book: Book):
        return (book.price * 25) / 100


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'isbn', 'description', 'genre', 'language', 'price', 'author')


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'description', 'genre', 'price', 'author')


class UserCreate(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']


class BookInstanceSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BookInstance
        fields = ['user_id', 'due_back', 'status', 'book', 'imprint', 'borrower']
