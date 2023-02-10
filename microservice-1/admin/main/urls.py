from django.contrib import admin
from django.urls import path, include
from .views import ProductViewSet, UserApiView


urlpatterns = [
    path('api/products/', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('api/products/<int:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('api/user', UserApiView.as_view())
]
