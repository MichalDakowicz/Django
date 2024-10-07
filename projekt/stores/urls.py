from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('store/<int:store_id>/', views.store_details, name='store_details'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('manager_list/', views.manager_list, name='manager_list'),
]