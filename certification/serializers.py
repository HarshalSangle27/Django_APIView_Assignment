from rest_framework import serializers
from .models import Certification

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__' # This automatically includes id, name, code, description, is_active, created_at, updated_at