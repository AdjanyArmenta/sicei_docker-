from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'school_id']  
        read_only_fields = ['id'] 
        extra_kwargs = {'name': {'required': False}, 'school_id': {'required': False}} 