# Generated by Django 5.0.4 on 2024-04-08 13:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='is_paid',
        ),
        migrations.AlterField(
            model_name='bill',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.customer'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
