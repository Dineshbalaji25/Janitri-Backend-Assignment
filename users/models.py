from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)

    groups = models.ManyToManyField(
        Group, 
        related_name="custom_user_set",  # Add a unique related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission, 
        related_name="custom_user_permissions_set",  # Add a unique related_name
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
