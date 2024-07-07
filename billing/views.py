from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import BillItemSerializer,BillSerializer,AnalyticsSerializer
from .models import Bill,BillItem
from django.db.models import Count,Sum
from rest_framework import permissions
class BillView(generics.ListCreateAPIView):
    queryset =Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes =[permissions.IsAuthenticated]

    def post(self,request,*args,**kwargs):
       try: 
         bill_serializer = self.get_serializer(data=request.data)
         if bill_serializer.is_valid():
            bill = bill_serializer.save()
            bill_items_data = bill_serializer.validated_data.pop('bill_items')  
            for item_data in bill_items_data:
                  BillItem.objects.create(bill=bill, **item_data) 
            return Response(bill_serializer.data, status=status.HTTP_201_CREATED)
         return Response(bill_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       except Exception as e:
          return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       

class AnalyticsApiView(generics.ListAPIView):
    serializer_class = AnalyticsSerializer
    permission_classes =[permissions.IsAuthenticated]

    def get_queryset(self):
         max_sales_employee = Bill.objects.values('employee__user__username').annotate(total_sales=Count('employee')).order_by('-total_sales').first()

         max_sales_product = BillItem.objects.values('product__name').annotate(total_sales=Sum('quantity')).order_by('-total_sales').first()

         return [{'max_sales_employee': max_sales_employee, 'max_sales_product': max_sales_product}]
   
