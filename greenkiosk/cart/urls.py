from django.urls import path
# from .views import add_to_cart
from .views import view_cart

urlpatterns = [
    # path('cart/add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # path('cart/add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/',view_cart,name='view_cart'),
]