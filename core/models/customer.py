from core.models.__base import BaseModel
from django.db import models


class Customer(BaseModel):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=30)  # TODO add phonenumber-field
    city = models.CharField(max_length=255, db_index=True)
    address = models.CharField(max_length=2000)
