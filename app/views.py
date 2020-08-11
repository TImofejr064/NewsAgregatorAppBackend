from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .source import updateNews

def index(request):
    return render(request, 'app/main_view.html')

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'category', 'image']
    serializer_class = CategorySerializer


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'headline', 'description', 'url_to_record', 'url_to_image', 'date', 'category']
    serializer_class = NewsSerializer

