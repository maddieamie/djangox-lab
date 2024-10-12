from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(default=date.today)
    pass

    def __str__(self):
        return f"{self.email}, {self.username}"
