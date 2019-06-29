from django.db import models
from django.urls import reverse


class Folder(models.Model):
    name = models.CharField(max_length=128)
    text_color = models.CharField(max_length=32, default='#000000', blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        full_name = f'{self.name}'
        if self.parent:
            full_name = f'{self.parent}::' + full_name
        return full_name

    @property
    def depth(self):
        if not self.parent:
            return 0
        else:
            return self.parent.depth + 1

    @property
    def get_list_url(self):
        return reverse('folder:list')

    def parent_url(self):
        url_list = []
        temp = self
        while(temp.parent):
            temp = temp.parent
            url_list.append(reverse('folder:list') + '?id=' + str(temp.pk))

        return url_list
