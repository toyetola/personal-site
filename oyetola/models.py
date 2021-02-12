from django.db import models
from django.utils import timezone
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    link = models.TextField(null=True)
    created_at = models.DateField(default=timezone.now, null=True)
    