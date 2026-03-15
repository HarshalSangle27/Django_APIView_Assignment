from rest_framework import serializers
from .models import ProductCourseMapping

class ProductCourseMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCourseMapping
        fields = '__all__'

    def validate(self, data):
        product = data.get('product')
        primary_mapping = data.get('primary_mapping', False)

        # Validation Rule: if one product already has a primary course mapping, 
        # another primary mapping for that same product should fail [cite: 75]
        if primary_mapping:
            # Check the database to see if this product already has a primary mapping
            existing_primary = ProductCourseMapping.objects.filter(product=product, primary_mapping=True)
            
            # If we are updating an existing record, we need to exclude ITSELF from the check
            if self.instance:
                existing_primary = existing_primary.exclude(pk=self.instance.pk)
                
            if existing_primary.exists():
                raise serializers.ValidationError({
                    "primary_mapping": "This product already has a primary course mapping."
                })

        return data