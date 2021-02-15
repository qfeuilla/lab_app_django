from django.db import models
from .types import MACHINE_TYPES

# Create your models here.
class Machine(models.Model):
    type = models.CharField(choices=MACHINE_TYPES, max_length=20)
    password = models.CharField(max_length=50, null=False, blank=False)
    machine_name = models.CharField(max_length=70, unique=True, null=False, blank=False)

# id, a type, a password and a name