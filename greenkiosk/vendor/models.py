from django.db import models

# Create your models here.
class Vendor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    password = models.CharField(max_length=100)


    def register(self):
        self.save

    def get_vendor_by_email(email):
        try:
            return Vendor.objects.get(email=email)
        except:
            return False
        

    def isExist(self):
        if Vendor.objects.filter(email = self.email):
             return True
        
        return False