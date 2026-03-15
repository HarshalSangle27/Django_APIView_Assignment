from django.db import models

# Create your models here.
from django.db import models
from core_project.base_models import TimeStampedModel
from product.models import Product
from course.models import Course

class ProductCourseMapping(TimeStampedModel):
    # Foreign keys linking to the master models [cite: 54, 55]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='course_mappings')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='product_mappings')
    
    primary_mapping = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True) 

    class Meta:
        # Validation Rule: Same product and course pair cannot be inserted twice 
        unique_together = ('product', 'course')

    def __str__(self):
        return f"{self.product.name} -> {self.course.name}"