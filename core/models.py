from django.db import models

# C

class GeneralSettings(models.Model):
    name = models.CharField(
        default= '',
        max_length= 254,
        blank=True,
    )
    description = models.CharField(
        default= '',
        max_length=254,
        blank=True,
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
    update_date = models.DateTimeField(
        blank=True,
        auto_now=True,
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
    )