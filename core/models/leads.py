from django.contrib.auth.models import User
from django.db import models

from core.constants import LeadStatus


class Lead(models.Model):
    title = models.CharField(max_length=255)
    reason = models.CharField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='leads', null=True)
    status = models.CharField(max_length=100, choices=LeadStatus.choices)
    customer = models.ForeignKey('core.Customer', on_delete=models.DO_NOTHING, related_name='leads')
    completion_date = models.DateField(null=True)
    address = models.CharField(max_length=2000)
    source = models.ForeignKey('core.Source', on_delete=models.DO_NOTHING, related_name='leads',
                               null=True)  # TODO убрать null
    work_type = models.CharField(max_length=255)





