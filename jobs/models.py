from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    name = models.CharField(max_length=50, null=True)
    def __str__ (self):
      return self.name