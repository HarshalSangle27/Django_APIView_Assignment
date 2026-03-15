from rest_framework import serializers
from .models import ProductCourseMapping

class ProductCourseMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCourseMapping
        fields = '__all__'

    def validate(self, data):
        product = data.get('product')
        primary_mapping = data.get('primary_mapping', False)

        
        
        if primary_mapping:
            
            existing_primary = ProductCourseMapping.objects.filter(product=product, primary_mapping=True)
            
            
            if self.instance:
                existing_primary = existing_primary.exclude(pk=self.instance.pk)
                
            if existing_primary.exists():
                raise serializers.ValidationError({
                    "primary_mapping": "This product already has a primary course mapping."
                })

        return data