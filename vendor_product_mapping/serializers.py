from rest_framework import serializers
from .models import VendorProductMapping

class VendorProductMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProductMapping
        fields = '__all__'

    def validate(self, data):
        vendor = data.get('vendor')
        primary_mapping = data.get('primary_mapping', False)

        # Validation Rule: if one vendor already has a primary product mapping, 
        # another primary mapping for that same vendor should fail [cite: 75]
        if primary_mapping:
            # Check the database to see if this vendor already has a primary mapping
            existing_primary = VendorProductMapping.objects.filter(vendor=vendor, primary_mapping=True)
            
            # If we are updating an existing record, we need to exclude ITSELF from the check
            if self.instance:
                existing_primary = existing_primary.exclude(pk=self.instance.pk)
                
            if existing_primary.exists():
                raise serializers.ValidationError({
                    "primary_mapping": "This vendor already has a primary product mapping."
                })

        return data