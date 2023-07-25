# views.py (Django example)
from django.shortcuts import render
from materiels.models import Materiel

def dashboardView(request):
    # Récupérer le nombre total de matériels enregistrés
    total_materiels = Materiel.objects.count()

    # Récupérer le nombre de matériels dont is_taken est False
    available_materiels = Materiel.objects.filter(is_taken=False).count()

    return render(request, 'dashboard.html', {'total_materiels': total_materiels, 'available_materiels': available_materiels})
