from django.urls import path
from .views import payment_upload_view
from .views import payment_list


urlpatterns = [
    path("payment/upload/",payment_upload_view,name="payment_upload_views"),

    path("products/list/", payment_list, name="product_list_view"),

]