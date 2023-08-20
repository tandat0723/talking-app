from django.urls import path, include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('categories', views.CategoryViewSet, 'category')
routers.register('banners', views.BannerViewSet, 'banner')
routers.register('products', views.ProductViewSet, 'product')
routers.register('brand', views.BrandViewSet, 'brand')
routers.register('comments', views.CommentViewSet, 'comment')
routers.register('users', views.UserViewSet, 'user')

urlpatterns = [
    path('', include(routers.urls))
]
