from django.db import models


from django.db import models
from core_project.base_models import TimeStampedModel

class Course(TimeStampedModel):
    
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True) 
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return f"{self.name} ({self.code})"
