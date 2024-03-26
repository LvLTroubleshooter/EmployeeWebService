from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee

def employee_list_json(request):
    employees = Employee.objects.all().values('name', 'position')
    return JsonResponse(list(employees), safe=False)


