from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import IndexEdit
from .forms import IndexEditForm
from django.urls import reverse
from django import forms
import markdown2
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView


class IndexView(ListView):
    """
    """
    template_name = "homepage/index.html"
    context_object_name = 'edit'

    def get_queryset(self):
        edit = IndexEdit.objects.all()
        for item in edit:
            item.content = markdown2.markdown(item.content, extras=['fenced-code-blocks'], )
        return edit


class IndexDetailView(FormView):
    """
    """
    form_class = IndexEditForm
    template_name = "homepage/index_detail.html"
    #success_url = "/index"

    
    def get_initial(self, **kwargs):           
        initial = {}
        with open('README.md') as f:
            initial['content'] = f.read()
        return initial

    
    def form_valid(self, form):

        indexedit = IndexEdit(id='1')
        indexedit.content = form.cleaned_data['content']
        indexedit.save()
        with open('README.md','w') as f:
            f.write(form.cleaned_data['content'])

        return HttpResponseRedirect('/index')



