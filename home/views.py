from django.shortcuts import render, redirect
from .models import CustomerModel, DepartmentModel
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    context = {
        'customers': CustomerModel.objects.all(),
        'departments': DepartmentModel.objects.all(),
    }
    if request.method == "POST":
      name = request.POST.get('username')
      email = request.POST.get('email')
      password = request.POST.get('password')
      department_id = request.POST.get('department')
      
      # Get department instance
      department = DepartmentModel.objects.get(department_id=department_id)
      
      customer = CustomerModel(name=name, email=email, password=password, department=department)
      customer.save()
      return HttpResponse("Customer Created Successfully")
    
    # if request.method == "GET":
    #   customer_id = request.GET.get('customer_id')
    #   customer = CustomerModel.objects.get(customer_id=customer_id)
    #   context['customer'] = customer
    #   return HttpResponse("Customer Retrieved Successfully")
    # if request.method == "PUT":
    #   customer_id = request.GET.get('customer_id')
    #   customer = CustomerModel.objects.get(customer_id=customer_id)
    #   name = request.POST.get('username')
    #   email = request.POST.get('email')
    #   password = request.POST.get('password')
    #   customer.name = name
    #   customer.email = email
    #   customer.password = password
    #   customer.save()
    #   return HttpResponse("Customer Updated Successfully")
    # if request.method == "DELETE":
    #   customer_id = request.GET.get('customer_id')
    #   customer = CustomerModel.objects.get(customer_id=customer_id)
    #   customer.delete()
    #   return HttpResponse("Customer Deleted Successfully")
    
    return render(request, 'index.html', context)