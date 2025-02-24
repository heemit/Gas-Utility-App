from rest_framework         import serializers
from django.contrib.auth    import get_user_model
from .models                import ServiceRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model   = get_user_model()
        fields  = ['id', 'username', 'email', 'phone']

class ServiceRequestSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model   = ServiceRequest
        fields  = ['id', 'user', 'request_type', 'description', 'attachment', 'status', 'created_at', 'updated_at']
