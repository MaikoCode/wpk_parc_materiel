# views.py (Django example)
from datetime import datetime
from django.shortcuts import render
from employe.models import Employe
from materiels.models import DemandeMateriel, Materiel, Categorie, SousCategorie
from facture.models import Facture
from django.db.models import Sum
from django.db.models import Count
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.role == 'ADMIN'

@login_required
@user_passes_test(is_admin)
def dashboardView(request):
    # Récupérer le nombre total de matériels enregistrés
    # total_materiels = Materiel.objects.count()
    # # Récupérer le nombre de matériels dont is_taken est False
    # available_materiels = Materiel.objects.filter(is_taken=False).count()

    total_materiels = Materiel.objects.all().count()
    available_materiels = Materiel.objects.filter(is_taken=False).count()
    total_employes = Employe.objects.all().count()
    total_factures = Facture.objects.all().count()
    categories = Categorie.objects.all()
    materiels_en_panne = Materiel.objects.filter(en_panne=True).count()
    # Calculate percentage of materiels en panne
    percentage_en_panne = (materiels_en_panne / total_materiels) * 100 if total_materiels > 0 else 0
    pending_requests = DemandeMateriel.objects.filter(status='pas encore traite').count()
    current_year = datetime.now().year
    montants_par_mois = Facture.objects.filter(date_facture__year=current_year).values('date_facture__month').annotate(total_montant=Sum('montant_total'))
    # Create a list to store the montants for each month (in the order of months)
    montants_list = [0] * 12
    for montant in montants_par_mois:
        month = montant['date_facture__month']
        montants_list[month - 1] = montant['total_montant']
    montants_list = [float(m) for m in montants_list]
    sous_categories = SousCategorie.objects.annotate(materiel_count=Count('materiel'))
    sous_category_names = [sous_category.nomSousCategory for sous_category in sous_categories]
    materiel_counts = [sous_category.materiel_count for sous_category in sous_categories]

    percentage_en_panne = round(percentage_en_panne, 2)
    context = {
        'total_materiels': total_materiels,
        'available_materiels': available_materiels,
        'total_employes': total_employes,
        'total_factures': total_factures,
        'categories': categories,
        'materiels_en_panne': materiels_en_panne,
        'percentage_en_panne': percentage_en_panne,
        'pending_requests': pending_requests,
        'montants_par_mois': montants_list,
        'sous_category_names': sous_category_names,
        'materiel_counts': materiel_counts,
    }
    return render(request, 'dashboard.html', context)


def error_404_view(request, exception):
    return render(request, '404.html', status=404)
