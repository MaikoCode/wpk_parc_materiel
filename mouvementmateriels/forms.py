from django import forms
from .models import MouvementMateriel, Materiel, Employe
from django.db.models import Q

class MouvementForm(forms.ModelForm):
    class Meta:
        model = MouvementMateriel
        fields = ['dateMouvement', 'dateRetour', 'description', 'employe', 'materiel']

    def __init__(self, *args, **kwargs):
        is_edit = kwargs.pop('is_edit', False)  # Retrieve the is_edit flag or default to False
        include_materiel = kwargs.pop('include_materiel', None)
        super().__init__(*args, **kwargs)

        # If the form is bound to an instance, ensure the instance's 'materiel' is included in the queryset
        if include_materiel is not None:
            # If 'include_materiel' is specified, add it to the queryset
            self.fields['materiel'].queryset = Materiel.objects.filter(
                Q(is_taken=False) | Q(pk=include_materiel.pk))
        else:
            # Otherwise, only include 'is_taken=False' materiels if it's not an edit operation
            if not is_edit:
                self.fields['materiel'].queryset = Materiel.objects.filter(is_taken=False)
                
        self.fields['employe'].queryset = Employe.objects.all()


class AffectationForm(forms.ModelForm):
    class Meta:
        model = MouvementMateriel
        fields = ['dateMouvement', 'description', 'employe']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employe'].queryset = Employe.objects.all()
        # self.fields['dateMouvement'].widget.attrs['class'] = 'form-control'  # Add form-control class for styling
        # self.fields['employe'].widget.attrs['class'] = 'form-control'  # Add form-control class for styling
