from django.urls import path
from .views import employee_list_json

urlpatterns = [
    path('api/employees/', employee_list_json, name='employee_list_json'),
]
