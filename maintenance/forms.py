from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Notesmaintenance

class NoteForm(forms.ModelForm):
    response_text = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Notesmaintenance
        fields = ['response_text']