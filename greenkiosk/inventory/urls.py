from django.urls import path
from .views import product_upload_view
from .views import products_list
from .views import product_detail
from .views import product_update_view
from .views import cart_list

urlpatterns = [
    path("products/upload/",product_upload_view,name="product_upload_views"),

    path("products/list/", products_list, name="product_list_view"),

    path("products/<int:id>/", product_detail, name="product_description_view"),

    path("inventory/products/edit/<int:id>/", product_update_view, name = "product_update"),

    path("cart/list",cart_list, name="cart_list_view"),
    
]

