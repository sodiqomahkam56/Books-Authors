from django.db import models

# Create your models here.


class Author(models.Model):
    full_name=models.CharField(max_length=100)
    birth_year=models.DateField()
    country=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

class Book(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.IntegerField()
    author=models.ForeignKey(Author,on_delete=models.PROTECT,related_name='book_author')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
