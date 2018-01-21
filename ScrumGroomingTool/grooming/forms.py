from django import forms
from .models import Grooming, ATDDCase


class GroomingEditForm(forms.ModelForm):

    class Meta:
        model = Grooming
        fields = ['title', 'sprint', 'item', 'scope','assumption', 'question', 'sw_cost_time', 'iv_cost_time']


class ATDDCaseForm(forms.ModelForm):

    class Meta:
        model = ATDDCase
        fields = ['suitename', 'grooming', 'case_file', 'case_content']

