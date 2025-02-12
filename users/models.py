from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date
from django.conf import settings  # Import settings to refer to the CustomUser model

# Custom user model
class CustomUser(AbstractUser):
    public_visibility = models.BooleanField(default=True)
    age = models.IntegerField(null=True, blank=True)
    birth_year = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    # Adding related_name to prevent reverse accessor clash
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='users_customuser_groups',  # Unique related_name for users
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='users_customuser_permissions',  # Unique related_name for users
        blank=True
    )

    def save(self, *args, **kwargs):
        if self.birth_year and not self.age:
            self.age = date.today().year - self.birth_year  # Calculate age based on the birth year
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

# UploadedFile model (correctly references the CustomUser)
from django.conf import settings
from django.db import models

class UploadedFile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    visibility = models.BooleanField(default=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    year_published = models.IntegerField()

    def __str__(self):
        return self.title
