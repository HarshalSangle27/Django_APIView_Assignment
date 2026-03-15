from django.db import models

# Create your models here.
from django.db import models
from core_project.base_models import TimeStampedModel

class Certification(TimeStampedModel):
    # Django automatically adds an 'id' AutoField as the primary key, so we don't need to write it.
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True) # Enforces the unique code validation
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True) # Bonus task: soft delete preparation

    def __str__(self):
        return f"{self.name} ({self.code})"
