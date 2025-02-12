from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

class CustomUser(AbstractUser):
    public_visibility = models.BooleanField(default=True)
    age = models.IntegerField(null=True, blank=True)
    birth_year = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    # Adding related_name to prevent reverse accessor clash
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='accounts_customuser_groups',  # Unique related_name for accounts
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='accounts_customuser_permissions',  # Unique related_name for accounts
        blank=True
    )

    def save(self, *args, **kwargs):
        if self.birth_year and not self.age:
            self.age = date.today().year - self.birth_year  # Calculate age based on the birth year
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
