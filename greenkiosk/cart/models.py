from django.db import models
from inventory.models import Product
from django.contrib.auth.models import User
from django.shortcuts import render,redirect


# Create your models here.
class Cart(models.Model):
    products = models.ManyToManyField(Product) 
    product = models.CharField(max_length=30)
    quantity = models.PositiveIntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def addProduct(request):
        user = request.user
        product_id = request.GET.get('product_id')
        product_cart = Product.objects.get(id=product_id)
        Cart(user=user, product=product_cart).save()
        return render(request, 'cart/addtocart.html')
    
  
       


