from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', views.ProductsViews, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path("categories/", views.api_categories),
    path("categories/<str:pk>", views.api_category),

]