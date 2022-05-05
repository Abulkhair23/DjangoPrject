from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.models import Book, Category, Author, BookCategory, BookAuthor
from core.serializers import BookSerializer, CategorySerializer, AuthorSerializer, \
    BookCategorySerializer, BookAuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCategoryViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    permission_classes = [IsAuthenticated]


class BookAuthorViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer
    permission_classes = [IsAuthenticated]


@api_view(('GET',))
@permission_classes((AllowAny,))
def categoryBooks(request, category_id):
    if request.method == "GET":
        books = BookCategory.objects.get_books(category_id)
        serializer = BookSerializer(instance=books, many=True)
        print(books)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(('GET',))
@permission_classes((AllowAny,))
def authorBooks(request, author_id):
    if request.method == "GET":
        books = BookAuthor.objects.get_books(author_id)
        serializer = BookSerializer(books, many=True)
        print(books)
        return Response(serializer.data, status=status.HTTP_200_OK)
