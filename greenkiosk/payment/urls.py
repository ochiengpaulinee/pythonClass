from django.urls import path
from .views import create_payment
from .views import payment_list
from .import views


urlpatterns = [
    path("payment/upload/",create_payment,name="payment_upload_views"),

    path("products/list/", payment_list, name="product_list_view"),

]