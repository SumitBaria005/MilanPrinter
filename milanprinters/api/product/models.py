from django.db import models
from api.category.models import Category
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    Category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    featuring = models.BooleanField(default=False, null=True)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    is_active = models.BooleanField(default=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
