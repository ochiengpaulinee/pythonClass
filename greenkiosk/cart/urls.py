from django.urls import path
from .views import create_cart, cart_list, cart_detail


urlpatterns = [
    path('carts/create/', create_cart, name='create_cart'),
    path('carts/', cart_list, name='cart_list'),
    path('carts/<int:cart_id>/', cart_detail, name='cart_detail'),
]


