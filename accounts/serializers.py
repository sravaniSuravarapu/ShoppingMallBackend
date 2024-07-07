from rest_framework import serializers
from .models import CustomUser
from customer.models import Customer
from employee.models import Employee
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True)
    password2 = serializers.CharField(write_only=True,required=True)

    class Meta :
        model = CustomUser
        fields =["username","email","password","password2","user_type"]

    def validate(self, attrs):
         if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password2": "Passwords does not matched!!."})
         if len(attrs['password']) < 8:
            raise serializers.ValidationError({"password": "Password must be at least 8 characters long."})
         if CustomUser.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email": "Email already exists."})
         return attrs
    
    def create(self, validated_data):
        user = CustomUser.objects.create(
            email =validated_data['email'],
            username=validated_data['username'],
            user_type =validated_data['user_type']
        )
        user.set_password(validated_data['password'])
        user.save()
        if validated_data['user_type'] == 'Employee':
            Employee.objects.create(user=user)
        else:
            Customer.objects.create(user=user)
        return user
    

class LoginSerializer(serializers.Serializer):
    username =serializers.CharField(max_length =100,write_only=True)
    password =serializers.CharField(max_length =100,write_only=True)

    def validate(self, attrs):
        username= attrs.get("username",None)
        password = attrs.get("password",None)

        if username is None : 
            raise serializers.ValidationError("Email should required for login")
        if password is None:
            raise serializers.ValidationError("Password should required for login")
        
        return attrs
    

