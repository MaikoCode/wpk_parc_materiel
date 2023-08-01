from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Materiel, Categorie, SousCategorie,DemandeMateriel
from .forms import MaterielForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import MaterielUpdateForm  # Use the updated form for the update view
from django.http import JsonResponse
from fournisseur.models import Fournisseur
import json
from .forms import DemandeMaterielForm
from django.views.generic import ListView

class MaterielListView(View):
    def get(self, request):
        categories = Categorie.objects.all()
        sub_categories = SousCategorie.objects.all()
        fournisseurs = Fournisseur.objects.all()
        # Convertir les données en JSON
        categories_json = [{'id': category.idCategory, 'nom': category.nomCategory} for category in categories]
        sub_categories_json = [{'id': sous_categorie.idSousCategorie, 'nom': sous_categorie.nomSousCategory, 'categorie': sous_categorie.categorie_id} for sous_categorie in sub_categories]
        form = MaterielForm()
        context = {
            'categories': categories,
            'sub_categories': sub_categories,
            'form': form,
            'categories_json': json.dumps(categories_json),
            'sub_categories_json': json.dumps(sub_categories_json),
            'fournisseurs': fournisseurs,
        }
        return render(request, 'materiels.html', context)

    def post(self, request):
        form = MaterielForm(request.POST)
        if form.is_valid():
            materiel_name = form.cleaned_data['materiel_name']
            materiel_description = form.cleaned_data['materiel_description']
            num_serie = form.cleaned_data['num_serie']
            materiel_description = form.cleaned_data['materiel_description']
            category_id = form.cleaned_data['categorie']
            sub_category_id = form.cleaned_data['sub_category']
            # Vérifier si une nouvelle catégorie a été spécifiée
            if category_id == 'new':
                nom_category = form.cleaned_data['new_category_name']
                description_category = form.cleaned_data['new_category_description']
                categorie = Categorie.objects.create(nomCategory=nom_category, description=description_category)
            else:
                categorie = Categorie.objects.get(idCategory=category_id)
            # Vérifier si une nouvelle sous-catégorie a été spécifiée
            if sub_category_id == 'new':
                nom_sous_category = form.cleaned_data['new_sub_category_name']
                description_sous_category = form.cleaned_data['new_sub_category_description']
                sous_categorie = SousCategorie.objects.create(nomSousCategory=nom_sous_category, description=description_sous_category, categorie=categorie)
            else:
                sous_categorie = SousCategorie.objects.get(idSousCategorie=sub_category_id)
            # Enregistrer le nouveau matériel
            Materiel.objects.create(nomMateriel=materiel_name, NumSerie=num_serie, description=materiel_description, sous_categorie=sous_categorie)
            messages.success(request, "Le matériel a été enregistré avec succès.")
            return redirect('materiel_list')
        # Si le formulaire n'est pas valide, réafficher le formulaire avec les erreurs
        categories = Categorie.objects.all()
        sub_categories = SousCategorie.objects.all()
        context = {
            'categories': categories,
            'sub_categories': sub_categories,
            'form': form
        }
        # Ajouter un message d'erreur à afficher
        messages.error(request, "Une erreur s'est produite lors de la soumission du formulaire.")
        return render(request, 'materiels.html', context)

def delete_materiel(request, materiel_id):
    materiel = get_object_or_404(Materiel, idMateriel=materiel_id)
    materiel_name = materiel.nomMateriel  # Get the name before deleting the object
    materiel.delete()
    messages.success(request, f"Le matériel {materiel_name} a été supprimé.")
    return redirect(reverse('materiel_list'))

def edit_materiel(request, materiel_id):
    materiel = Materiel.objects.get(idMateriel=materiel_id)
    print(materiel.description)
    if request.method == 'POST':
        form = MaterielUpdateForm(request.POST)
        if form.is_valid():
            # Update the employee details
            materiel.nomMateriel = form.cleaned_data['materiel_name']
            materiel.NumSerie = form.cleaned_data['num_serie']
            materiel.description = form.cleaned_data['materiel_description']
            materiel.save()
            print("Le materiel est  modifie " )
            messages.success(request, "Les infos de l'employé " + materiel.nomMateriel  +" sont modifiés")
    return redirect('materiel_list')

# Utilisez la classe basée sur les vues pour votre vue MaterielListView_User
class MaterielListView_User(View):
    def get(self, request):
        categories = Categorie.objects.all()
        sub_categories = SousCategorie.objects.all()
        fournisseurs = Fournisseur.objects.all()
        materiels = Materiel.objects.all()
        demandes = DemandeMateriel.objects.all()
        # Convertir les données en JSON
        categories_json = [{'id': category.idCategory, 'nom': category.nomCategory} for category in categories]
        sub_categories_json = [{'id': sous_categorie.idSousCategorie, 'nom': sous_categorie.nomSousCategory, 'categorie': sous_categorie.categorie_id} for sous_categorie in sub_categories]
        form = MaterielForm()
        context = {
            'categories': categories,
            'sub_categories': sub_categories,
            'form': form,
            'categories_json': json.dumps(categories_json),
            'sub_categories_json': json.dumps(sub_categories_json),
            'fournisseurs': fournisseurs,
            'demandes': demandes,  
        }
        return render(request, 'materiels_user.html', context)

def demander_materiel(request):
    if request.method == 'POST':
        form = DemandeMaterielForm(request.POST)
        if form.is_valid():
            date_debut = form.cleaned_data['date_debut']
            description = form.cleaned_data['description']
            materiel_id = form.cleaned_data['materiel']
            demandeur_id = form.cleaned_data['demandeur']
            nouvelle_demande = DemandeMateriel.objects.create(
                date_debut=date_debut,
                description=description,
                materiel=materiel_id,
                demandeur=demandeur_id
            )
            nouvelle_demande.save()
            # Rediriger l'utilisateur vers la page de confirmation ou une autre vue appropriée
            messages.success(request, 'La demande a été envoyée avec succès.')
            return redirect('materiels_user')
        else:
            # Le formulaire n'est pas valide, afficher les erreurs dans les messages framework
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        # Si la méthode est GET, afficher le formulaire vide
        form = DemandeMaterielForm()
    return redirect('materiels_user')

class Gestion_Demande(ListView):
    model = DemandeMateriel
    template_name = 'gestion_demande.html'
    context_object_name = 'demandes'

    def get(self, request):
        demandes=DemandeMateriel.objects.all()
        l=["ID demande",
            "Date de début d'utilisation",
            "Description de la demande",
            "nom materiel",
            "N° Série matériel",
            "Description",
            "disponibilité",
            "Statut",
            "Actions"]
        context = {'titles':l, 'demandes':demandes}
        return render(request, 'gestion_demande.html', context)

    def post(self, request, *args, **kwargs):
        demande_id = request.POST.get('demande_id')
        action = request.POST.get('action')
        demande = DemandeMateriel.objects.get(id=demande_id)
        if action == 'valider':
            # Mettre à jour le statut de la demande
            demande.status = 'Validee'
            demande.save()
            messages.success(request, f'Demande {demande.id} validée avec succès.')
        elif action == 'rejeter':
            # Mettre à jour le statut de la demande
            demande.status = 'Rejetee'
            demande.save()
            messages.warning(request, f'Demande {demande.id} rejetée.')
        return render(request, self.template_name, {'demandes': self.get_queryset()})

def accepter_demande(request, demande_id):
    demande = get_object_or_404(DemandeMateriel, id=demande_id)
    # Mettre à jour le statut de la demande en "Acceptée"
    demande.status = "Acceptée"
    demande.save()
    # Afficher un message de succès
    messages.success(request, "La demande a été acceptée avec succès.")
    # Rediriger l'utilisateur vers la même page
    return redirect(request.META['HTTP_REFERER'])  

def rejeter_demande(request, demande_id):
    demande = get_object_or_404(DemandeMateriel, id=demande_id)
    demande.status = "Rejetée"
    demande.save()
    # Afficher un message de succès
    messages.success(request, "La demande a été rejetée.")
    # Rediriger l'utilisateur vers la même page
    return redirect(request.META['HTTP_REFERER'])  