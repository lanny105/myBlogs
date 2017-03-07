from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class article(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-publish_date']


