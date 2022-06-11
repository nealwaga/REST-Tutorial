from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Employees
from .serializer import EmployeesSerializer

from rest_framework.views import APIView #used so the normal views can return API data
from rest_framework.response import Response #where you get back the status or a particular response(if it's okay it will return 200)
from rest_framework import status #basically send back the status


# Create your views here.
class EmployeeList(APIView):

    #to return all employees in the model
    def get(self, request):
        employess1 = Employees.objects.all() #variable to store all my objects
        serializer = EmployeesSerializer(employess1, many=True) #taking all objects & converting them to JSON
        return Response(serializer.data)


    #to create a new employee
    def post(self):
        pass