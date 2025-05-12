from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import JsonResponse
from .services import CustomerService, DepartmentService
from .models import CustomerModel, DepartmentModel
from django.shortcuts import render, redirect

class CustomerListView(ListView):
    template_name = 'index.html'
    context_object_name = 'customers'
    # model = CustomerModel
    
    def get_queryset(self):
        return CustomerModel.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['customers'] = CustomerService.get_all_customers()
            context['departments'] = DepartmentService.get_all_departments()
            return context
        except Exception as e:
            messages.error(self.request, str(e))
            return context

class CustomerDetailView(DetailView):
    template_name = 'customer_detail.html'
    context_object_name = 'customer'
    
    def get_object(self):
        customer_id = self.kwargs.get('pk')
        return CustomerService.get_customer_by_id(customer_id)


class CustomerCreateView(CreateView):
    template_name = 'customer_form.html'
    success_url = reverse_lazy('customer-list')
    
    def post(self, request, *args, **kwargs):
        try:
            data = {
                'name': request.POST.get('username'),
                'email': request.POST.get('email'),
                'password': request.POST.get('password'),
                'department_id': request.POST.get('department')
            }
            CustomerService.create_customer(data)
            messages.success(request, 'Customer created successfully')
            return redirect(self.success_url)
        except Exception as e:
            messages.error(request, str(e))
            return render(request, self.template_name, {'departments': DepartmentService.get_all_departments()})


class CustomerUpdateView(UpdateView):
    template_name = 'customer_form.html'
    success_url = reverse_lazy('customer-list')
    
    def get(self, request, *args, **kwargs):
        try:
            customer = CustomerService.get_customer_by_id(kwargs.get('pk'))
            context = {
                'customer': customer,
                'departments': DepartmentService.get_all_departments()
            }
            return render(request, self.template_name, context)
        except Exception as e:
            messages.error(request, str(e))
            return redirect('customer-list')
    
    def post(self, request, *args, **kwargs):
        try:
            data = {
                'name': request.POST.get('username'),
                'email': request.POST.get('email'),
                'password': request.POST.get('password'),
                'department_id': request.POST.get('department')
            }
            CustomerService.update_customer(kwargs.get('pk'), data)
            messages.success(request, 'Customer updated successfully')
            return redirect(self.success_url)
        except Exception as e:
            messages.error(request, str(e))
            return redirect('customer-list')

class CustomerDeleteView(DeleteView):
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('customer-list')
    
    def get(self, request, *args, **kwargs):
        try:
            customer = CustomerService.get_customer_by_id(kwargs.get('pk'))
            return render(request, self.template_name, {'customer': customer})
        except Exception as e:
            messages.error(request, str(e))
            return redirect('customer-list')
    
    def post(self, request, *args, **kwargs):
        try:
            CustomerService.delete_customer(kwargs.get('pk'))
            messages.success(request, 'Customer deleted successfully')
            return redirect(self.success_url)
        except Exception as e:
            messages.error(request, str(e))
            return redirect('customer-list')