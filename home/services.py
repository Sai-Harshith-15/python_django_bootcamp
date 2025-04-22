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
      



# #####################################


# from django.views.generic import ListView, DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from django.contrib import messages
# from django.shortcuts import render, redirect
# from .services import CustomerService, DepartmentService

# class CustomerListCreateView(ListView):
#     template_name = 'index.html'
#     context_object_name = 'customers'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         try:
#             context['customers'] = CustomerService.get_all_customers()
#             context['departments'] = DepartmentService.get_all_departments()
#             return context
#         except Exception as e:
#             messages.error(self.request, str(e))
#             return context
    
#     def post(self, request, *args, **kwargs):
#         try:
#             data = {
#                 'name': request.POST.get('username'),
#                 'email': request.POST.get('email'),
#                 'password': request.POST.get('password'),
#                 'department_id': request.POST.get('department')
#             }
#             CustomerService.create_customer(data)
#             messages.success(request, 'Customer created successfully')
#             return redirect('customer-list')
#         except Exception as e:
#             messages.error(request, str(e))
#             return self.get(request, *args, **kwargs)

# class CustomerDetailUpdateDeleteView(DetailView):
#     template_name = 'customer_detail.html'
#     context_object_name = 'customer'
    
#     def get_object(self):
#         customer_id = self.kwargs.get('pk')
#         return CustomerService.get_customer_by_id(customer_id)
    
#     def post(self, request, *args, **kwargs):
#         action = request.POST.get('action')
        
#         if action == 'update':
#             return self.update(request)
#         elif action == 'delete':
#             return self.delete(request)
#         return redirect('customer-list')
    
#     def update(self, request):
#         try:
#             data = {
#                 'name': request.POST.get('username'),
#                 'email': request.POST.get('email'),
#                 'password': request.POST.get('password'),
#                 'department_id': request.POST.get('department')
#             }
#             CustomerService.update_customer(self.kwargs.get('pk'), data)
#             messages.success(request, 'Customer updated successfully')
#             return redirect('customer-list')
#         except Exception as e:
#             messages.error(request, str(e))
#             return self.get(request)
    
#     def delete(self, request):
#         try:
#             CustomerService.delete_customer(self.kwargs.get('pk'))
#             messages.success(request, 'Customer deleted successfully')
#             return redirect('customer-list')
#         except Exception as e:
#             messages.error(request, str(e))
#             return self.get(request)