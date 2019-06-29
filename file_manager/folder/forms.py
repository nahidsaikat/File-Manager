from django.forms import ModelForm

from file_manager.folder.models import Folder


class FolderForm(ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'text_color', 'parent']
