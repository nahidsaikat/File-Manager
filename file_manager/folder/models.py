from django.db import models


class Folder(models.Model):
    name = models.CharField(max_length=128)
    text_color = models.CharField(max_length=32, default='#000000', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
