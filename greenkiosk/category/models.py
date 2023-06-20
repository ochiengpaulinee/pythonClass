from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=20)



    def all_categories():
        return Category.objects.all()
    def __str__(self):
        return self.category_name
