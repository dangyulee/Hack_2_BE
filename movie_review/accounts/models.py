from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
  REQUIRED_FIELDS = []
  email = None
  nickname = models.CharField(max_length=30, default='default_nickname')