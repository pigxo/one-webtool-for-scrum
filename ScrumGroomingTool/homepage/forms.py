from django import forms
from .models import IndexEdit



class IndexEditForm(forms.ModelForm):

    class Meta:
        model = IndexEdit
        fields = ['content']
        widgets = {
            'content': forms.Textarea({'rows':50, 'cols': 80}),
        }

