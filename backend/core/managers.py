from django.db import models


class BookCategoryManager(models.Manager):
    def get_books(self, category_id):
        books = [i.book for i in self.get_queryset().filter(category=category_id)]
        return books

    def get_categories(self, book_id):
        categories = [i.category for i in self.get_queryset().filter(book=book_id)]
        return categories


class BookAuthorManager(models.Manager):
    def get_books(self, author_id):
        books = [i.book for i in self.get_queryset().filter(author=author_id)]
        return books

    def get_authors(self, book_id):
        authors = [i.author for i in self.get_queryset().filter(book=book_id)]
        return authors
