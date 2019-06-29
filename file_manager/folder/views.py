from django.views.generic import ListView, CreateView

from file_manager.folder.forms import FolderForm
from file_manager.folder.models import Folder


class FolderCreateView(CreateView):
    form_class = FolderForm
    template_name = 'folder/add.html'


class FolderListView(ListView):
    context_object_name = 'folder_list'
    template_name = 'folder/list.html'

    def get_queryset(self):
        return Folder.objects.filter(parent=None).all()
