from django.db import models

# Create your models here.


class Owner(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.name
