from django.views.generic import ListView, CreateView

from file_manager.folder.forms import FolderForm


class FolderCreateView(CreateView):
    form_class = FolderForm
    template_name = ''
