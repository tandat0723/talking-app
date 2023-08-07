from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from .models import User, Category, Brand, Product


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
