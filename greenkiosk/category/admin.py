from django.contrib import admin

# Register your models here.
from .models import Category




class Product_Category(admin.ModelAdmin):
    list_display = ["category_name"]

admin.site.register(Category,Product_Category)