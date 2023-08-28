from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Notesmaintenance

class NoteForm(forms.ModelForm):
    response_text = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Notesmaintenance
        fields = ['response_text']


class DescriptionmaintenanceForm(forms.Form):
    description = forms.CharField(widget=SummernoteWidget())

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def init(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().init(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result