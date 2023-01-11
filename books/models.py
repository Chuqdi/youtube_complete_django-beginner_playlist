from django.db import models
from django.utils import timezone

class Book(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    date_created = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.name