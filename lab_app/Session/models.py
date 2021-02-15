from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from .flags import FLAGS

# Create your models here.
class Result(models.Model):
    results = models.TextField()

# Create your models here.
class Session(models.Model):
    docker = models.FileField()
    token = models.CharField(max_length=15, unique=True, validators=[MinLengthValidator(15)])
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.OneToOneField(Result, null=True, default=None, on_delete=models.CASCADE, editable=False)
    flag = models.CharField(choices=FLAGS, max_length=25, editable=False, default=FLAGS[0][0])
