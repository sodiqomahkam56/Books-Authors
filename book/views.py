from django.shortcuts import render

from .models import Book


# Create your views here.

def get_book(request):
    books=Book.objects.all()
    context={
        'books':books
    }
    return render(request,'book/book_list.html',context)


def book_detail(request,pk):
    book=Book.objects.get(pk=pk)
    context={
        'book':book
    }
    return render(request,'book/book_detail.html',context)
