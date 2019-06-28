from django.views.generic import CreateView, ListView

from file_manager.file.forms import FileForm
from file_manager.file.models import File


class FileCreateView(CreateView):
    form_class = FileForm
    template_name = 'file/add.html'


class FileListView(ListView):
    queryset = File.objects.all()
    context_object_name = 'file_list'
    template_name = 'file/list.html'
