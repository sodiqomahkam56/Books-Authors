from django.contrib import admin

from book.models import Book, Author

admin.site.register(Author)
admin.site.register(Book)
