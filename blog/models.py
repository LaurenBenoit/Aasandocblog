from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    name = models.ForeignKey('auth.User')
    specialization = models.CharField(max_length=200)
    history = models.TextField()
    added_date = models.DateTimeField(
            default=timezone.now)
    verified_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title