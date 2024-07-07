from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from django.core.exceptions import ObjectDoesNotExist
class CustomerUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class =CustomerSerializer
    # permission_classes =[permissions.IsAuthenticated]
    def update(self, request, *args, **kwargs):
       try: 
        instance =self.get_object()
        serializer = self.get_serializer(instance,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       except Exception as e:
          return Response({"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
    def destroy(self, request, *args, **kwargs):
       try:
            instance = self.get_object()
            instance.delete()
            return Response({"message": "Employee deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
       except ObjectDoesNotExist:
            return Response({"error": "Employee does not exist."}, status=status.HTTP_404_NOT_FOUND)
       except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)