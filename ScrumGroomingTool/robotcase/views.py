from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.views.generic.list import ListView
from .models import RobotCase
from grooming.models import Grooming

# Create your views here.

def read_file(filename, buf_size=8192):
    with open(filename, "rb") as f:
        while True:
            content = f.read(buf_size)
            if content:
                yield content
            else:
                break

def file_download(request, case_name=None):
    filename = './robotcase/robotcase_storage/'+ case_name
    #response = HttpResponse(read_file(filename),mimetype='application/octet-stream')
    #response['Content-Disposition'] = 'attachment; filename=%s' %filename
    response = StreamingHttpResponse(read_file(filename))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(case_name)
    return response


class IndexView(ListView):
    template_name = "robotcase/robotcase_index.html"
    context_object_name = 'cases'

    def get_queryset(self):
        cases = Grooming.objects.all()
        return cases