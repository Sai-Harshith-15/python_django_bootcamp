from rest_framework import serializers
from .models import CustomerModel, DepartmentModel

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentModel
        fields = ['department_id', 'department_name']

class CustomerSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    
    class Meta:
        model = CustomerModel
        fields = ['customer_id', 'name', 'email', 'password', 'department']
        
    