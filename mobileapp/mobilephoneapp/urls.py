from django.urls import path
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('categories', views.CategoryViewSet, 'category')

urlpatterns = [
    path('', views.index, name="index")
]
