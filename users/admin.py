from django.contrib import admin
from .models import CustomUser, UploadedFile  # Import your models here

# Register your models here
admin.site.register(CustomUser)
admin.site.register(UploadedFile)
