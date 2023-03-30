from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Author, Book, BookInstance, LibraryUser


# Register your models here.
@admin.register(LibraryUser)
class User(UserAdmin):
    pass


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookInstance)
