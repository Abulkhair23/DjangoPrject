from django.urls import path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('profile', ProfileViewSet)
urlpatterns = router.urls

urlpatterns += [
    path('create/', create_user)
]
