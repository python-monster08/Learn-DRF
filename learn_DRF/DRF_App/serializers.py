from rest_framework import serializers

#  Create Your Serializers here...
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)