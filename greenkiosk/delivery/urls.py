from django.urls import path
from .views import delivery_upload_view


urlpatterns = [
    path("delivery/upload/",delivery_upload_view,name="delivery_upload_view"),
]