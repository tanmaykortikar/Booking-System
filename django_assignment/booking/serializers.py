from rest_framework import serializers
from .models import CustomUser, Resource, Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
     # Add fields from the related resource
    resource_name = serializers.CharField(source='resource.name')
    resource_description = serializers.CharField(source='resource.description')

    class Meta:
        model = Booking
        fields = ['id', 'resource_name', 'resource_description', 'booking_date', 'quantity_booked']