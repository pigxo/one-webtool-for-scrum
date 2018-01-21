from __future__ import unicode_literals

from django.db import models
from grooming.models import Grooming

# Create your models here.

class RobotCase(models.Model):
    """
    """
    grooming = models.ForeignKey(Grooming,verbose_name = 'Grooming', on_delete = models.CASCADE)

    def save(self):
        super().save()

