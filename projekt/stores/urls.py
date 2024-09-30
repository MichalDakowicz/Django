from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('store/<int:store_id>/', views.store_details, name='store_details'),
]