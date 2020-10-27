from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='st'),
    path('store/', views.store, name='st'),
    path('cart/', views.cart, name='ct'),
    path('checkout/', views.checkout, name='cout'),
    path('update_item/', views.updateItem, name='UI'),
]
