from rest_framework import serializers
from .models import Bill, BillItem

class BillItemSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(source='get_total_price', read_only=True,max_digits=10, decimal_places=2)

    def get_total_price(self, obj):
        return obj.quantity * obj.unit_price

    class Meta:
        model = BillItem
        fields = ('id', 'product', 'quantity', 'unit_price', 'total_price')

class BillSerializer(serializers.ModelSerializer):
    bill_items = BillItemSerializer(many=True)

    class Meta:
        model = Bill
        fields = '__all__'
        # exclude =["total_amount"]



class AnalyticsSerializer(serializers.Serializer):
    max_sales_employee = serializers.DictField()
    max_sales_product = serializers.DictField()