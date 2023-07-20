from django import forms
from .models import MouvementMateriel
from employe.models import Employe
from materiels.models import Materiel
from django.db.models import Q

class MouvementForm(forms.ModelForm):
    class Meta:
        model = MouvementMateriel
        fields = ['dateMouvement', 'dateRetour', 'description', 'employe', 'materiel']
    # def _init_(self, *args, **kwargs):
    #     super()._init_(*args, **kwargs)
    #     # Filter the queryset for the 'materiel' field to show only materials with 'is_taken=False'
    #     self.fields['materiel'].queryset = Materiel.objects.filter(is_taken=False)
    #     # Create the 'employe' dropdown with all employee names
    #     self.fields['employe'].queryset = Employe.objects.all()

    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['required'] = 'required'

    def _init_(self, *args, **kwargs):
        include_materiel = kwargs.pop('include_materiel', None)
        super()._init_(*args, **kwargs)

        # If the form is bound to an instance, ensure the instance's 'materiel' is included in the queryset
        if include_materiel is not None:
            # If 'include_materiel' is specified, add it to the queryset
            self.fields['materiel'].queryset = Materiel.objects.filter(
                Q(is_taken=False) | Q(pk=include_materiel.pk))
        else:
            # Otherwise, only include 'is_taken=False' materiels
            self.fields['materiel'].queryset = Materiel.objects.filter(is_taken=False)
        
        self.fields['employe'].queryset = Employe.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['required'] = 'required'