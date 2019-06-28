from django.db import models

from file_manager.folder.models import Folder


class File(models.Model):
    name = models.CharField(max_length=128)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    path = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
