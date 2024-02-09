from rest_framework import serializers
from .models import Student

# Create Your Serializers Here...

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    def update(self, instance, validated_data):
        # print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        # print(instance.name)
        # print(instance.roll)
        instance.roll = validated_data.get('roll', instance.roll)
        # print(instance.roll)
        # print(instance.city)
        instance.city = validated_data.get('city', instance.city)
        # print(instance.city)
        instance.save()
        return instance