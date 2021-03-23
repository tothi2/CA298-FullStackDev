from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# product
# id
# name
# description
# price

class CaUser(AbstractUser):
    is_admin = models.BooleanField(default=False)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.FileField(upload_to='product_img/', blank=True)


class ShoppingBasket(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(CaUser, on_delete=models.CASCADE)

class ShoppingBasketItems(models.Model):
    id = models.AutoField(primary_key=True)
    basket_id = models.ForeignKey(ShoppingBasket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(CaUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    shipping_addr = models.CharField(max_length=500)
    date_created = models.DateField(auto_now_add=True)

class OrderItems(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def price(self):
        return self.product.price * self.quantity





