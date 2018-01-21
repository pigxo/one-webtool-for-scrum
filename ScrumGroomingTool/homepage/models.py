from django.db import models


class IndexEdit(models.Model):
    """
    """
    content = models.TextField(verbose_name='')

    def save(self):
        super().save()
