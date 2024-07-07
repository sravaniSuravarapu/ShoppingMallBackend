from django.contrib import admin

# Register your models here.
from .models import Bill

class BillAdmin(admin.ModelAdmin):
    list_display = ["created_at"]
    ordering = ["-created_at"]

admin.site.register(Bill,BillAdmin)