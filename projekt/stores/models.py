from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.store.name}"
    
class Manager(models.Model):
    employees = models.ManyToManyField(Employee)
    store = models.OneToOneField(Store, on_delete=models.CASCADE)

    def __str__(self):
        employee_names = ", ".join([f"{employee.first_name} {employee.last_name}" for employee in self.employees.all()])
        return f"{self.store.name} - {employee_names}"