from django.db import models
from customer.models import Customer
from products.models import Product
from employee.models import Employee

class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True) 
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    def save(self, *args, **kwargs):
        self.total_amount = sum(item.total_price for item in self.bill_items.all())
        super().save(*args, **kwargs)

class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE,related_name="bill_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.unit_price
        super().save(*args, **kwargs)
