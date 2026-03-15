from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__' # This automatically includes id, name, code, description, is_active, created_at, updated_at