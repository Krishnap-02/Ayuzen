from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='products/')
    price=models.DecimalField(decimal_places=2,max_digits=7)
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)


    def __str__(self):
        return self.name