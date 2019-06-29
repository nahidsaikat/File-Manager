from django.db import models

from file_manager.folder.models import Folder


class File(models.Model):
    name = models.CharField(max_length=128)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    path = models.CharField(max_length=128, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    @property
    def full_path(self):
        return f'{self.folder}::{self.name}'

    @property
    def extension(self):
        return str(self.name).split('.')[-1]

    @property
    def icon(self):
        if self.extension == 'txt':
            return '-alt'
        elif self.extension == 'pdf':
            return '-pdf'
        elif self.extension in ['doc', 'docs', 'docx', 'odt', 'dot', 'dotm', 'dotx']:
            return '-word'
        elif self.extension in ['xls', 'xlsx', 'xlt']:
            return '-excel'
        elif self.extension in ['ppt', 'pptx', 'ppsx']:
            return '-powerpoint'
        elif self.extension in ['png', 'jpg', 'jpeg']:
            return '-image'
        elif self.extension in ['mp4', 'mkv', 'flv', 'vob', 'avi', 'wmv']:
            return '-video'
        elif self.extension in ['mp3', 'aa', 'aac', 'act', 'mmf', 'mpc']:
            return '-audio'
        elif self.extension in ['py', 'js', 'java', 'php', 'rb', 'html', 'css', 'htm']:
            return '-code'
        elif self.extension in ['zip', 'rar', 'iso', '7z', 'apk']:
            return '-archive'
        elif self.extension == 'csv':
            return '-csv'
        else:
            return ''
