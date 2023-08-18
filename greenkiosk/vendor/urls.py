from django.urls import path
from .views import vendor_upload_view

urlpatterns = [
    path("vendor/upload/",vendor_upload_view,name="vendor_upload_view"),

]