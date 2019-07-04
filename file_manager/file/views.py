import os
from wsgiref.util import FileWrapper

from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.views.generic.base import View

from file_manager.file.forms import FileForm
from file_manager.file.models import File


class FileCreateView(CreateView):
    form_class = FileForm
    template_name = 'file/add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_url'] = reverse('file:add')
        context['add_folder'] = reverse('folder:add')
        context['add_file'] = reverse('file:add')
        return context

    def get_success_url(self):
        return reverse('folder:list')

    def post(self, request, *args, **kwargs):
        return super().post(request=request, args=args, **kwargs)


class FileListView(ListView):
    queryset = File.objects.all()
    context_object_name = 'file_list'
    template_name = 'file/list.html'


class FileDownloadView(View):

    def get(self, request, pk):
        file = File.objects.filter(pk=pk).first()
        filename = file.file.path
        wrapper = FileWrapper(file.file)
        response = HttpResponse(wrapper, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename=%s' % file.name
        response['Content-Length'] = os.path.getsize(filename)
        return response
