from django.urls import path
from .views import get_book, book_detail

urlpatterns = [
    path('',get_book,name='book-list'),
    path('books/<int:pk>/', book_detail, name='book-detail')
]
