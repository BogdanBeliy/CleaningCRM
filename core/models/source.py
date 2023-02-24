from django.contrib.auth.models import User
from django.db import models
from core.models.__base import BaseModel


class Source(BaseModel):
    name = models.CharField(max_length=255)
    token = models.CharField(max_length=255, unique=True, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='sources', null=True)
