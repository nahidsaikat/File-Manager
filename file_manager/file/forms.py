from django.forms import ModelForm

from file_manager.file.models import File


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['name', 'folder']
