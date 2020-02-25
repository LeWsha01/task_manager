from django.db import models

from django.conf import settings


class Project(models.Model):
    name = models.CharField(
        max_length=128
    )
    description = models.TextField(
        max_length=1000
    )
    rate = models.IntegerField(null=True)


class Issue(models.Model):
    name = models.CharField(
        max_length=128
    )
    description = models.TextField(
        max_length=2000
    )
    created_at = models.DateTimeField(
        auto_created=True
    )
    reported = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='reporters',
    )
    assigne = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='assigns'
    )
    deadline = models.DateField(
        null=False,
        blank=False
    )
