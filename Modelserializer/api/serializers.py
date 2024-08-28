from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['name', 'rolls','city']
        extra_kwargs={'name': {'read_only':True}}
    #field level validation same
    