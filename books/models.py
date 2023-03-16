from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Book(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    date_created = models.DateField(default=timezone.now)

    creator = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self) -> str:
        return self.name