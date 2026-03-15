from django.db import models

# Create your models here.
from django.db import models
from core_project.base_models import TimeStampedModel
from course.models import Course
from certification.models import Certification

class CourseCertificationMapping(TimeStampedModel):
    # Foreign keys linking to the master models [cite: 54, 55]
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='certification_mappings')
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE, related_name='course_mappings')
    
    primary_mapping = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True) 

    class Meta:
        # Validation Rule: Same course and certification pair cannot be inserted twice 
        unique_together = ('course', 'certification')

    def __str__(self):
        return f"{self.course.name} -> {self.certification.name}"