from django.urls import reverse
from django.views.generic import ListView, CreateView

from file_manager.folder.forms import FolderForm
from file_manager.folder.models import Folder
from file_manager.file.forms import FileForm
from file_manager.file.models import File


class FolderCreateView(CreateView):
    form_class = FolderForm
    template_name = 'folder/add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_url'] = reverse('folder:add')
        context['add_folder'] = reverse('folder:add')
        context['add_file'] = reverse('file:add')
        return context

    def get_success_url(self):
        return reverse('folder:list')


class FolderListView(ListView):
    context_object_name = 'folder_list'
    template_name = 'folder/list.html'

    def get_queryset(self):
        pk = self.request.GET.get('id')
        queryset = Folder.objects.all()
        if pk:
            queryset = queryset.filter(parent__pk=pk)
        else:
            queryset = queryset.filter(parent=None)

        order_by = self.request.GET.get('sort')
        if order_by == 'time':
            queryset = queryset.order_by('-created_at')
        elif order_by == 'name':
            queryset = queryset.order_by('name')

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        pk = self.request.GET.get('id')

        context['file_list'] = self.get_file_query(pk)
        context['add_folder'] = reverse('folder:add')
        context['add_file'] = reverse('file:add')
        context['parent_folder'] = self.get_parent_folder_link(pk)

        return context

    def get_file_query(self, pk):
        file_query = File.objects.all()
        if pk:
            file_query = file_query.filter(folder__pk=pk)
        else:
            file_query = file_query.filter(folder=None)
        order_by = self.request.GET.get('sort')
        if order_by == 'time':
            file_query = file_query.order_by('-created_at')
        elif order_by == 'name':
            file_query = file_query.order_by('name')
        return file_query

    @staticmethod
    def get_parent_folder_link(pk):
        parent_folder = []
        if pk:
            folder = Folder.objects.get(pk=pk)
            parent_folder.append({
                'text': folder.name,
                'link': reverse('folder:list') + f'?id={folder.pk}',
            })
            while folder.parent:
                parent_folder.append({
                    'text': folder.parent.name,
                    'link': reverse('folder:list') + f'?id={folder.parent.pk}',
                })
                folder = folder.parent
            parent_folder.reverse()
        return parent_folder
