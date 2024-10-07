from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Employee, Store, Manager

def home_page(request):
    return render(request, 'stores/index.html')

def employee_list(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'stores/employee_list.html', context)

def store_details(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    return render(request, 'stores/store_details.html', context={'store': store})

def manager_list(request):
    managers = Manager.objects.all()
    context = {'managers': managers}
    
    return render(request, 'stores/manager_list.html', context)