from rest_framework import serializers
from .models import Student

# Create Your Serializers Here....

# validator
def start_with_k(value):
    if value[0].lower() != 'k':
        raise serializers.ValidationError('Name must be start with K')

class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[start_with_k])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
    
    # Field level Validation
    def validate_roll(self, value):
        if value>=200:
            raise serializers.ValidationError('Seat Full')
        return value

    # Object Level Validation
    def validate(self, attrs):
        nm = attrs.get('name')
        ct = attrs.get('city')
        if nm.lower()=="kamlesh" and ct.lower() != "bhopal":
            raise serializers.ValidationError("City must be Bhopal")
        return attrs