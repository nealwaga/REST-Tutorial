from dataclasses import fields
from rest_framework import serializers
from .models import Employees


#Create here
class EmployeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employees
        fields = '__all__'