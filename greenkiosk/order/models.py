from django.db import models
from customer.models import Customer
from cart.models import Cart
from delivery.models import Delivery

# Create your models here.
class Order(models.Model):
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100)

    customer = models.ForeignKey(Customer,null=True,on_delete = models.CASCADE)
    cart = models.ForeignKey(Cart,null=True,on_delete=models.CASCADE)
    delivery = models.OneToOneField(Delivery,null=True,on_delete=models.CASCADE)
