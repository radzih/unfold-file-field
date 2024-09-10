from django.contrib import admin
from unfold.admin import ModelAdmin

from djangoProject1.models import File


@admin.register(File)
class FileAdmin(ModelAdmin):
    list_display = ('id', )
