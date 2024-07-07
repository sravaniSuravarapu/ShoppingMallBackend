from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
CustomUser = get_user_model()
class Customer(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    phonenumber = models.CharField(max_length=12)
    shipping_address_line1 = models.CharField(max_length=255)
    shipping_address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user.username
