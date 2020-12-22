from django.db import models
from api.user.models import User
from api.product.models import Product

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    product_name = models.CharField(max_length=100)
    no_of_copies = models.CharField(max_length=100, default=0)
    transaction_id = models.CharField(max_length=100, default=0)
    total_amount = models.CharField(max_length=100, default=0)
    written_image = models.ImageField(
        upload_to='images/', blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
