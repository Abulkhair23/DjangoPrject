import os

from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError
from .managers import *

ALLOWED_EXTENSIONS = ['.pdf']


def validate_extension(value):
    split_ext = os.path.splitext(value.name)
    if len(split_ext) > 1:
        ext = split_ext[1]
        if ext.lower() not in ALLOWED_EXTENSIONS:
            raise ValidationError(f'not allowed file, valid extensions: {ALLOWED_EXTENSIONS}')


class Book(models.Model):
    name = models.CharField(max_length=100, blank=True, default="")
    description = models.TextField(max_length=1000, blank=True, default="")
    pages = models.IntegerField(blank=True, default=0)
    src = models.FileField(blank=True, null=True, upload_to='files/', validators=[validate_extension, ])

    def authors(self):
        authors = [i.author for i in self.getAuthors.all()]
        print(authors)
        return authors

    def categories(self):
        categories = [i.category for i in self.getCategories.all()]
        print(categories)
        return categories


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, default="")


class Author(models.Model):
    first_name = models.CharField(max_length=100, blank=True, default="")
    last_name = models.CharField(max_length=100, blank=True, default="")
    about = models.TextField(max_length=1000, blank=True, default="")


class BookCategory(models.Model):
    book = models.ForeignKey(Book, related_name="getCategories", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="books", on_delete=models.CASCADE)
    objects = BookCategoryManager()

    class Meta:
        unique_together = ['book', 'category']


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, related_name="getAuthors", on_delete=models.CASCADE)
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
    objects = BookAuthorManager()

    class Meta:
        unique_together = ['book', 'author']
