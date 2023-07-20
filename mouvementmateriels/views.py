from django.shortcuts import get_object_or_404, render, redirect
from .forms import MouvementForm

from django.contrib import messages

from django.core.paginator import Paginator

from mouvementmateriels.models import MouvementMateriel

def mouvements(request):
    if request.method == 'POST':
        form = MouvementForm(request.POST)
        try:
            if form.is_valid():
                # date_mouvement = form.cleaned_data['dateMouvement']
                # date_retour = form.cleaned_data['dateRetour']
                # description = form.cleaned_data['description']
                # employe = form.cleaned_data['employe']
                materiel = form.cleaned_data['materiel']
                materiel.is_taken = True
                materiel.save()
                form.save()
                messages.success(request, 'Un nouveau mouvement est ajouté.')
                return redirect('mouvements')
        except Exception as e:
            messages.error(request, 'Une erreur est survenur lors de l\'ajout d\'un mouvement')
    form = MouvementForm()
    get_mouvements =  MouvementMateriel.objects.all()
    
    #pagination
    page = Paginator(get_mouvements, 1)
    page_liste = request.GET.get('page')
    page = page.get_page(page_liste) 
    return render(request, 'mouvements.html', {'page': page,'form': form })


def delete_mouvement(request, idMouvement):
    mouvement = MouvementMateriel.objects.get(idMouvement=idMouvement)
    materiel = mouvement.materiel
    materiel.is_taken=False
    materiel.save()
    mouvement.delete()
    messages.success(request, "Le mouvement a été supprimé avec succes")
    return redirect('mouvements')
    

def edit_mouvement(request, idMouvement):
    return redirect('mouvements')

# def edit_mouvement(request, idMouvement):
#     if request.method == 'POST':
#         form = MouvementForm(request.POST)  # Replace "YourFormName" with the actual name of your form
#         if form.is_valid():
#             date_mouvement = form.cleaned_data['dateMouvement']
#             # date_retour = form.cleaned_data['dateRetour']
#             # description = form.cleaned_data['description']
#             # employe = form.cleaned_data['employe']
#             # materiel = form.cleaned_data['materiel']
#             # Do whatever you want with the form data here, for example, print them
#             print("Date Mouvement:", date_mouvement)
#             # print("Date Retour:", date_retour)
#             # print("Description:", description)
#             # print("Employé:", employe)
#             # print("Matériel:", materiel)
#         mouvement = MouvementMateriel.objects.get(idMouvement=idMouvement)
#         print(mouvement.description)
#     return redirect('mouvements')