from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Employee, Store

def employee_list(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'stores/index.html', context)

def store_details(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    return HttpResponse(f"Szczegóły sklepu: {store.name} ({store.location})")