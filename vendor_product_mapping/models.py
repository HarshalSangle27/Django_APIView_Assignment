from django.db import models

# Create your models here.
from django.db import models
from core_project.base_models import TimeStampedModel
from vendor.models import Vendor
from product.models import Product

class VendorProductMapping(TimeStampedModel):
    # Foreign keys linking to the master models [cite: 54, 55]
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='product_mappings')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='vendor_mappings')
    
    primary_mapping = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True) 

    class Meta:
        # Validation Rule: Same vendor and product pair cannot be inserted twice 
        unique_together = ('vendor', 'product')

    def __str__(self):
        return f"{self.vendor.name} -> {self.product.name}"