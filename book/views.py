from django.shortcuts import render

from .models import Book


# Create your views here.

def get_book(request):
    books=Book.objects.all()
    context={
        'books':books
    }
    return render(request,'book/book_list.html',context)
