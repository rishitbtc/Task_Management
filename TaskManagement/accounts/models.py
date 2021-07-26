from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

Role = (
        ('Project Manager', 'Project Manager'),
        ('Employee', 'Employee'),
    )


class User(AbstractUser):
    first_name = models.CharField(max_length=122, null=True, blank=True)
    last_name = models.CharField(max_length=122, null=True, blank=True)
    contact = PhoneNumberField()
    role = models.CharField(max_length=50, choices=Role, null=True, blank=True)

    def __str__(self):
        return self.first_name
