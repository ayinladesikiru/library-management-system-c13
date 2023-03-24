from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.BookCreateApiView.as_view()),
    # path('books/', views.BookListView.as_view()),
]