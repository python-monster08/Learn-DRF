from rest_framework import serializers
from .models import Student

# Create your Serializers Here...
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']
        fields = '__all__'

        