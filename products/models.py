from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="Images/",blank=True,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.IntegerField(default=0)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.name