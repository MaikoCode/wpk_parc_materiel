from django.shortcuts import render, redirect
from .models import Panne
from materiels.models import Materiel
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db.models import Q
import csv
from django.http import HttpResponse
from django.core.paginator import Paginator
from .forms import PanneForm

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
    materiels_en_panne = Materiel.objects.filter(en_panne=True)

    pannes = Panne.objects.none()  # Créez un queryset vide
    for materiel in materiels_en_panne:
        pannes_materiel = Panne.objects.filter(materiel=materiel, resolue=False)
        pannes = pannes.union(pannes_materiel)  # Combinez les queryset

    search_query = request.GET.get('search_query')

    if search_query:
        pannes = pannes.filter(
            Q(materiel__nomMateriel__icontains=search_query) |
            Q(materiel__NumSerie__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(date_panne__icontains=search_query),
            resolue=False
        )

    paginator = Paginator(pannes, 2)  # Montrer 10 pannes par page
    page_number = request.GET.get('page')
    pannes = paginator.get_page(page_number)

    pannes_passees = Panne.objects.filter(resolue=True)

    if request.method == 'POST':
        form = PanneForm(request.POST)
        if form.is_valid():
            panne = form.save(commit=False)
            panne.user = request.user
            panne.materiel.en_panne = True  # Mettre le matériel en état de panne
            panne.materiel.save()  # Sauvegarder l'état du matériel
            panne.save()
    else:
        form = PanneForm()

    return render(request, 'panne.html',
                  {'pannes': pannes, 'search_query': search_query, 'pannes_passees': pannes_passees, 'form': form})

@require_POST
def toggle_panne(request, panne_id):
    panne = Panne.objects.get(id=panne_id)
    panne.resolue = True
    panne.materiel.en_panne = False  # Pour mettre à jour l'état du matériel correspondant
    panne.materiel.save()  # Sauvegarder les modifications du matériel
    panne.save()  # Sauvegarder les modifications de la panne
    return redirect('pannes')
