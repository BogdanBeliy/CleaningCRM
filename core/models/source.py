from django.db import models


class Source(models.Model):
    name = models.CharField(max_length=255)
    token = models.CharField(max_length=255, unique=True, null=True)


