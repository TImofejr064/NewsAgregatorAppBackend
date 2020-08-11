from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers

urlpatterns = [
    path('', index, name="main")
]

router = routers.DefaultRouter()
router.register('api/categories', CategoryViewSet)
router.register('api/news', NewsViewSet)

urlpatterns += router.urls
