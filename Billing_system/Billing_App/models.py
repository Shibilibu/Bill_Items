from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=55,decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Bill(models.Model):
    items = models.ManyToManyField(Item)
    total_cost = models.DecimalField(max_digits=55,decimal_places=2)


    def __str__(self):
        return f"Bill ID: {self.id}"


class Login(models.Model):
    username = models.CharField(max_length=65)
    password = models.CharField(max_length=55)
    usertype = models.CharField(max_length=55,default=1)
