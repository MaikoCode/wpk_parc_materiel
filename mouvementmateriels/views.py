from datetime import date
from django.shortcuts import get_object_or_404, render, redirect

from materiels.models import Materiel
from .forms import AffectationForm, MouvementForm

from django.contrib import messages

from django.core.paginator import Paginator

from mouvementmateriels.models import MouvementMateriel

from django.db.models import Q

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

    # Handle search query
    search_query = request.GET.get('search_query')
    get_mouvements = get_filtered_mouvement(search_query)

    # get_mouvements =  MouvementMateriel.objects.all()
    
    #pagination
    page = Paginator(get_mouvements, 3)
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
    mouvement = MouvementMateriel.objects.get(idMouvement=idMouvement)
    if request.method == 'POST':
        form = MouvementForm(request.POST, include_materiel=mouvement.materiel, is_edit=True)
        if form.is_valid():
            date_mouvement = form.cleaned_data['dateMouvement']
            date_retour = form.cleaned_data['dateRetour']
            description = form.cleaned_data['description']
            print("Date Mouvement:", date_mouvement)
            print("type: ", type(date_mouvement))
            print("Date Retour:", date_retour)
            print("type: ", type(date_retour))
            print("Description:", description)
            print('mater: ', mouvement.materiel.nomMateriel)
            mouvement.dateMouvement = date_mouvement
            mouvement.dateRetour = date_retour
            mouvement.description = description
            mouvement.save()
            messages.success(request, 'Le mouvement est modifié avec success.')
        else:
            print('Form not valid:', form.errors)  # print form errors here
            messages.error(request, 'formulaire non valide')
        mouvement = MouvementMateriel.objects.get(idMouvement=idMouvement)
        print(mouvement.description)
    return redirect('mouvements')


def affecter_mouvement(request, idMouvement):
    mouvement = MouvementMateriel.objects.get(idMouvement=idMouvement)
    if request.method == 'POST':
        form = AffectationForm(request.POST)
        if form.is_valid():
            date_mouvement = form.cleaned_data['dateMouvement']
            desc = form.cleaned_data['description']
            employe = form.cleaned_data['employe']
            print('employe: ',employe.nom)
            print('desc: ',desc)
            print('date mouv: ', date_mouvement)
            mouvement.actionType = "Retour"
            mouvement.dateRetour = date.today()
            mouvement.save()

            materiel_instance = mouvement.materiel
            employe_instance = employe

            newMouvement = MouvementMateriel(
                dateMouvement=date_mouvement,
                dateRetour=None,
                description=desc,
                employe=employe_instance,
                materiel=materiel_instance,
                actionType="acquisition"
            )
            newMouvement.save()
            messages.success(request, 'Le mouvement matériel est  affecté avec success.')
        else:
            messages.error(request, 'Une erreur est rencontré')

            
    return redirect('mouvements')

    
def get_filtered_mouvement(search_query):
    if search_query:
        return MouvementMateriel.objects.filter(
            Q(idMouvement__icontains=search_query) |
            Q(description__icontains=search_query) |                           
            Q(employe__nom__icontains=search_query) |
            Q(employe__prenom__icontains=search_query) |                  
            Q(materiel__nomMateriel__icontains=search_query) |                
            Q(materiel__NumSerie__icontains=search_query) |                   
            Q(materiel__sous_categorie__nomSousCategory__icontains=search_query) |   
            Q(materiel__sous_categorie__categorie__nomCategory__icontains=search_query) | 
            Q(actionType__icontains=search_query) |
            Q(dateMouvement__icontains=search_query)                         
        ).order_by('idMouvement')
    else:
        return MouvementMateriel.objects.all().order_by('idMouvement')
