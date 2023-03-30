from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('authors', views.AuthorViewSet)
router.register('book-instances', views.BookInstanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('author/<int:pk>/', views.author_detail, name='author-detail'),
    path('book-authors/', views.BookAuthorView.as_view()),
    path('books/', views.BookListView.as_view()),
    path('books/<int:pk>/', views.BookDetailView.as_view()),
]