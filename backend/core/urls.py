from django.urls import path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('books', BookViewSet)
router.register('authors', AuthorViewSet)
router.register('categories', CategoryViewSet)
router.register('book_categories', BookCategoryViewSet)
router.register('book_authors', BookAuthorViewSet)
urlpatterns = router.urls

urlpatterns += [
    path('authors/<int:author_id>/books/', authorBooks),
    path('categories/<int:category_id>/books/', categoryBooks)
]
