from .models import CustomerModel, DepartmentModel
from .serializer import CustomerSerializer, DepartmentSerializer
from django.shortcuts import get_object_or_404

class CustomerService:
    @staticmethod
    def get_all_customers():
        customers = CustomerModel.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return serializer.data
      
    @staticmethod
    def get_customer_by_id(customer_id):
        try:
            customer = get_object_or_404(CustomerModel, customer_id=customer_id)
            serializer = CustomerSerializer(customer)
            return serializer.data
        except Exception as e:
            raise Exception(f"Error fetching customer: {str(e)}")
    
    @staticmethod
    def create_customer(data):
        try:
            department = DepartmentModel.objects.get(department_id=data['department_id'])
            customer = CustomerModel.objects.create(
                name=data['name'],
                email=data['email'],
                password=data['password'],
                department=department
            )
            serializer = CustomerSerializer(customer)
            return serializer.data
        except Exception as e:
            raise Exception(f"Error creating customer: {str(e)}")
          
    @staticmethod
    def update_customer(customer_id, data):
        try:
            customer = get_object_or_404(CustomerModel, customer_id=customer_id)
            department = DepartmentModel.objects.get(department_id=data['department_id'])
            
            customer.name = data.get('name', customer.name)
            customer.email = data.get('email', customer.email)
            customer.password = data.get('password', customer.password)
            customer.department = department
            customer.save()
            
            serializer = CustomerSerializer(customer)
            return serializer.data
        except Exception as e:
            raise Exception(f"Error updating customer: {str(e)}")
    
    @staticmethod
    def delete_customer(customer_id):
        try:
            customer = get_object_or_404(CustomerModel, customer_id=customer_id)
            customer.delete()
            return True
        except Exception as e:
            raise Exception(f"Error deleting customer: {str(e)}")

class DepartmentService:
    @staticmethod
    def get_all_departments():
        departments = DepartmentModel.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return serializer.data
      
    def get_department_by_id(department_id):
      try:
        department = get_object_or_404(department_id=department_id)
        serializer = DepartmentSerializer(department)
        return serializer.data
      except Exception as e:
        raise Exception(f"Error fetching department: {str(e)}")
      
    @staticmethod
    def create_department(data):
      try:
        department = DepartmentModel.objects.create(
          department_name=data['department_name']
        )
        serializer = DepartmentSerializer(department)
        return serializer.data
      except Exception as e:
        raise Exception(f"Error creating department: {str(e)}")
      
    @staticmethod
    def update_department(department_id, data):
      try:
        department = get_object_or_404(DepartmentModel, department_id=department_id)
        
        department.department_name = data.get('department_name', department.department_name)
        department.save()
        
        
        serializer = DepartmentSerializer(department)
        return serializer.data
      except Exception as e:
        raise Exception(f"Error updating department: {str(e)}")
            
