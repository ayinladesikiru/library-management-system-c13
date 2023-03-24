from django.db import models
from uuid import uuid4


# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    date_of_death = models.DateField(blank=True, null=True, default='0000-10-01')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    isbn = models.CharField(max_length=13, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    date_added = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='authors')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, related_name='genres')
    language = models.ForeignKey('Language', on_delete=models.CASCADE, related_name='languages')

    def __str__(self):
        return self.title


class Genre(models.Model):
    GENRE_CHOICE = [
        ('FINANCE', 'FIN'),
        ('POLITICS', 'POL'),
        ('POWER', 'POW'),
        ('COMEDY', 'COM'),
    ]
    name = models.CharField(max_length=10, choices=GENRE_CHOICE, default='FIN')

    def __str__(self):
        return self.name


class Language(models.Model):
    LANGUAGE_CHOICES = [
        ('YORUBA', 'YOR'),
        ('IGBO', 'IGB'),
        ('HAUSA', 'HAU'),
        ('ENGLISH', 'ENG')
    ]
    name = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='YOR')

    def __str__(self):
        return self.name


class BookInstance(models.Model):
    STATUS_CHOICES = [
        ('AVAILABLE', 'A'),
        ('BORROWED', 'B')
    ]
    unique_id = models.UUIDField(primary_key=True, default=uuid4)
    due_back = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='A')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='books')
    imprint = models.CharField(max_length=55, null=False, blank=False)

    def __str__(self):
        return self.imprint
