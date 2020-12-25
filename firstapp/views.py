from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
# Create your views here.
def employee(request):
    emp = {
        'id': 1,
        'name': 'sugimoto',
        'features': 'immortal',
        'loves': 'asirpa',
    }
    data = Employee.objects.all()
    response = {
        'employees': list(data.values('name','features','loves'))
    }
    return JsonResponse(data=response)