from django.db import models

# Create your models here.

class CustomerModel(models.Model):
    customer_id = models.AutoField(primary_key=True)
    department = models.ForeignKey('DepartmentModel', on_delete=models.CASCADE, related_name='customers')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
      
class DepartmentModel(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name