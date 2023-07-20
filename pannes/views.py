from django.shortcuts import render, redirect
from .models import Panne
from materiels.models import Materiel
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db.models import Q
import csv
from django.http import HttpResponse


# @login_required
# def historique_pannes_page(request):
#     # Récupérer toutes les pannes, résolues et non résolues
#     pannes = Panne.objects.all()

#     return render(request, 'historique_pannes.html', {'pannes': pannes})


def download_pannes_csv(request):
    pannes = Panne.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="pannes.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nom du matériel', 'Date de la panne', 'Status'])

    for panne in pannes:
        status = 'Résolue' if panne.resolue else 'Non résolue'
        writer.writerow([panne.materiel.nomMateriel, panne.date_panne, status])

    return response

def pannes_page(request):
    # Récupérer tous les matériels en panne
    materiels_en_panne = Materiel.objects.filter(en_panne=True)

    # Pour chaque matériel en panne, vérifier s'il y a déjà une panne existante pour ce matériel.
    # Si ce n'est pas le cas, créer une nouvelle panne.
    for materiel in materiels_en_panne:
        if not Panne.objects.filter(materiel=materiel, resolue=False).exists():
            Panne.objects.create(materiel=materiel, description="Description de la panne...")
            # Apres il faudra remplace description par // description=materiel.description

    # Récupérer la requête de recherche
    search_query = request.GET.get('search_query')

    if search_query:
        # Si une recherche a été effectuée, filtrer les pannes non résolues en fonction de la requête de recherche
        pannes = Panne.objects.filter(
            Q(materiel_nomMateriel_icontains=search_query) |  # recherche dans le nom du materiel
            Q(materiel_NumSerie_icontains=search_query) |  # recherche dans le numéro de série du matériel
            Q(description__icontains=search_query) |  # recherche dans la description
            Q(date_panne__icontains=search_query),  # recherche dans la date de la panne
            resolue=False  # on ne veut que les pannes non résolues
        )
    else:
        # Récupérer toutes les pannes non résolues pour les afficher
        pannes = Panne.objects.filter(resolue=False)
        
    pannes_passees = Panne.objects.filter(resolue=True)

    return render(request, 'panne.html', {'pannes': pannes, 'search_query': search_query, 'pannes_passees': pannes_passees})

@require_POST
def toggle_panne(request, panne_id):
    panne = Panne.objects.get(id=panne_id)
    panne.resolue = True
    panne.materiel.en_panne = False  # Pour mettre à jour l'état du matériel correspondant
    panne.materiel.save()  # Sauvegarder les modifications du matériel
    panne.save()  # Sauvegarder les modifications de la panne
    return redirect('pannes')