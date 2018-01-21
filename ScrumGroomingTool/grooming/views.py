from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Grooming,ATDDCase, Feature
from .forms import  GroomingEditForm,ATDDCaseForm
from django.urls import reverse
from django import forms
import markdown2
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, UpdateView
from .plugin import grooming2robot
from django.shortcuts import render


class GroomingIndexView(ListView):
    template_name = "grooming/grooming_index.html"
    def get_queryset(self):
        grooming_list = Grooming.objects.all()
        return grooming_list


class GroomingDetailView(DetailView):
    """
    """
    model = Grooming
    template_name = "grooming/grooming_detail.html"
    context_object_name = "grooming_detail"
    pk_url_kwarg = 'grooming_id'
    
    def  convert_markdown_split_line(self, mark_string):
        return mark_string.replace('\n','  \n')

    def get_object(self, queryset=None):
        obj = super(GroomingDetailView, self).get_object()
        obj.scope = markdown2.markdown(self.convert_markdown_split_line(obj.scope), extras=['fenced-code-blocks'], )
        obj.question = markdown2.markdown(self.convert_markdown_split_line(obj.question), extras=['fenced-code-blocks'], )
        obj.assumption = markdown2.markdown(self.convert_markdown_split_line(obj.assumption), extras=['fenced-code-blocks'], )
        obj.content = markdown2.markdown(self.convert_markdown_split_line(obj.content), extras=['fenced-code-blocks'],)
        #obj.atdd = obj.atddcase_set.all()
        #obj.atdd = []
        #for atdd in obj.atddcase_set.all():
        #    obj.atdd.append(atdd.suitename)
        return obj  

    def get_context_data(self, **kwargs):
        current_id = self.object.id
        lens = len(Grooming.objects.all())
        kwargs['grooming_detail_next'] = str(self.object.id +1) if current_id < lens else str(lens)
        kwargs['grooming_detail_pre'] = str(self.object.id - 1) if current_id > 1 else '1'
        return super(GroomingDetailView, self).get_context_data(**kwargs)


class GroomingCreateView(FormView):
    """
    """
    form_class = GroomingEditForm
    template_name = "grooming/grooming_create.html"

    def form_valid(self, form):
        grooming = form.save()
        robot_case_name = grooming2robot.GroomingAtddToRobot(grooming).generate_robot_case()
        grooming.case_file = robot_case_name.split('/')[-1]
        grooming.save()
        return HttpResponseRedirect('/grooming/index/')



class GroomingDetailEditView(UpdateView):
    """
    """
    model = Grooming
    form_class = GroomingEditForm
    template_name = 'grooming/grooming_create.html'

    def form_valid(self, form):
        grooming = form.save()
        robot_case_name = grooming2robot.GroomingAtddToRobot(grooming).generate_robot_case()
        grooming.case_file = robot_case_name.split('/')[-1]
        grooming.save()
        return HttpResponseRedirect('../')
    #success_url = '../'



class FeatureIndexView(ListView):
    template_name = "grooming/feature_index.html"
    def get_queryset(self):
        feature_list = Feature.objects.all()
        return feature_list



class AddATDDView(FormView):
    """
    """
    model = ATDDCase
    form_class = ATDDCaseForm
    template_name = "atdd/new_atdd_org.html"
    pk_url_kwarg = 'grooming_id'

    def form_valid(self, form):
        print(form)
        atdd = form.save()
        pk = self.kwargs.get(self.pk_url_kwarg, None) 
        atdd.grooming_belong_to=Grooming.objects.get(id=pk)
        atdd.save()
        return HttpResponseRedirect('../')




def add_atdd(request):

    return render(request, 'atdd/new_atdd.html')


class ATDDDetailView(DetailView):
    """
    """
    model = ATDDCase
    template_name = "atdd/atdd_detail.html"
    context_object_name = "atdd_detail"
    pk_url_kwarg = 'atdd_id'

    def get_queryset(self):
        atdd_list = ATDDCase.objects.all()
        return atdd_list
    
    def  convert_markdown_split_line(self, mark_string):
        return mark_string.replace('\n','  \n')

    def get_object(self, queryset=None):
        obj = super(ATDDDetailView, self).get_object()
        obj.suitename = markdown2.markdown(self.convert_markdown_split_line(obj.suitename), extras=['fenced-code-blocks'], )
        obj.testname = markdown2.markdown(self.convert_markdown_split_line(obj.testname), extras=['fenced-code-blocks'], )
        #obj.question = markdown2.markdown(self.convert_markdown_split_line(obj.question), extras=['fenced-code-blocks'], )
        #obj.assumption = markdown2.markdown(self.convert_markdown_split_line(obj.assumption), extras=['fenced-code-blocks'], )
        return obj  

    def get_context_data(self, **kwargs):
        current_id = self.object.id
        lens = len(ATDDCase.objects.all())
        kwargs['atdd_detail_next'] = str(self.object.id +1) if current_id < lens else str(lens)
        kwargs['atdd_detail_pre'] = str(self.object.id - 1) if current_id > 1 else '1'
        return super(ATDDDetailView, self).get_context_data(**kwargs)


