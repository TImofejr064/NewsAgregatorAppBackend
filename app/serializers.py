from rest_framework.serializers import ModelSerializer

from .models import *

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category', 'category_for_api', 'image']

class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'headline', 'description', 'url_to_record', 'url_to_image', 'date', 'category']