from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.

class Cart(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)

    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    quantity=models.PositiveBigIntegerField(default=1)


    def __str__(self):
        return f"{self.product.name} - {self.quantity}"