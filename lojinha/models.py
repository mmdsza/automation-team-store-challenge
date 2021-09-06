from django.db import models

# Create your models here.

class Produto(models.Model):
    class ProductSize(models.TextChoices):
        Small = 'S', 'Small'
        Medium = 'M', 'Medium'
        Large = 'L', 'Large'
    name = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    size = models.CharField(
        max_length=1,
        choices = ProductSize.choices,
        default = ProductSize.Small)
