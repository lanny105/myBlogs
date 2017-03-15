from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from sorl.thumbnail import ImageField

# Create your models here.

class article(models.Model):
    author = models.ForeignKey('auth.User', null=True)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, blank=False)
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    visit = models.IntegerField(default=0)
    image = models.ImageField(upload_to='temp/img/', null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-publish_date']


