from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # This is the magic line. It tells Django NOT to create a database table 
        # for this model, but to use it as a template for other models.
        abstract = True