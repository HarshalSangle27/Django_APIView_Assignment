from rest_framework import serializers
from .models import CourseCertificationMapping

class CourseCertificationMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCertificationMapping
        fields = '__all__'

    def validate(self, data):
        course = data.get('course')
        primary_mapping = data.get('primary_mapping', False)

        
        
        if primary_mapping:
            
            existing_primary = CourseCertificationMapping.objects.filter(course=course, primary_mapping=True)
            
            
            if self.instance:
                existing_primary = existing_primary.exclude(pk=self.instance.pk)
                
            if existing_primary.exists():
                raise serializers.ValidationError({
                    "primary_mapping": "This course already has a primary certification mapping."
                })

        return data