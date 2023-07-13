from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Ticket
from .models import Response
from employe.models import Employe

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority', 'files']
        widgets = {
            'description': SummernoteWidget(),
            'files': MultipleFileInput(),
        }

    files = MultipleFileField(required=False)

    def clean_files(self):
        files = self.cleaned_data.get('files')
        if files and len(files) > 5:
            raise forms.ValidationError("You can upload up to 5 files.")
        return files

class DescriptionForm(forms.Form):
    description = forms.CharField(widget=SummernoteWidget())

class ResponseForm(forms.ModelForm):
    response_text = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Response
        fields = ['response_text']
    
class TicketFilterForm(forms.Form):
    employee = forms.ModelChoiceField(
        queryset=Employe.objects.all(), 
        required=False, 
        label="Filter by Employee",
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Choose an Employee"
    )
    employee.label_from_instance = lambda obj: f"{obj.nom} {obj.prenom}"

    status = forms.ChoiceField(
        choices=[('', 'All'), ('open', 'Open'), ('in_progress', 'en cours'), ('completed', 'completed')],
        required=False, 
        label="Filter by Status",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    priority = forms.ChoiceField(
        choices=[('', 'All'), ('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
        required=False, 
        label="Filter by Priority",
        widget=forms.Select(attrs={'class': 'form-control'})
    )