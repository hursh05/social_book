from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UploadedFile

@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'visibility', 'year_published', 'cost')
    search_fields = ('title', 'description', 'user__username')
