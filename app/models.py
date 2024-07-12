from django.db import models
from django.utils import timezone

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    book_title = models.CharField(max_length=250)
    book_name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    file = models.FileField(upload_to='books/pdfs', default='books/pdfs/default.pdf')
    image = models.ImageField(upload_to='books/images', default='books/images/default.png')
    search_count = models.IntegerField(default=0)
    Category = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=20)
    Publication_Country = models.CharField(max_length=100)
    Language = models.CharField(max_length=50)
    Publication_Year = models.IntegerField()

    def __str__(self):
        return self.book_title
