from rest_framework import serializers
from .models import CourseCertificationMapping

class CourseCertificationMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCertificationMapping
        fields = '__all__'

    def validate(self, data):
        course = data.get('course')
        primary_mapping = data.get('primary_mapping', False)

        # Validation Rule: if one course already has a primary certification mapping, 
        # another primary mapping for that same course should fail [cite: 75]
        if primary_mapping:
            # Check the database to see if this course already has a primary mapping
            existing_primary = CourseCertificationMapping.objects.filter(course=course, primary_mapping=True)
            
            # If we are updating an existing record, we need to exclude ITSELF from the check
            if self.instance:
                existing_primary = existing_primary.exclude(pk=self.instance.pk)
                
            if existing_primary.exists():
                raise serializers.ValidationError({
                    "primary_mapping": "This course already has a primary certification mapping."
                })

        return data