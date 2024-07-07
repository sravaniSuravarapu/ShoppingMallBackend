
from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()
class Employee(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    positon = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date_of_hire = models.DateField(auto_now_add=True)

    def __str__(self) :
        return self.user.username