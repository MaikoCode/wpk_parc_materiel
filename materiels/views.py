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
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse



def search_materials(request):
    if request.method == 'POST':
        query = request.POST.get('query', '').strip()

        materials = Materiel.objects.filter(
            Q(nomMateriel__icontains=query) |
            Q(NumSerie__icontains=query) |
            Q(description__icontains=query)
        )

        categories = [material.sous_categorie.categorie for material in materials]
        sub_categories = [material.sous_categorie for material in materials]

        selected_categorie_ids = [categorie.idCategory for categorie in categories]  # Convertir l'objet en liste d'IDs
        selected_Sous_categorie_ids = [sub_categorie.idSousCategorie for sub_categorie in sub_categories]

        context = {
            'categories': categories,
            'sub_categories': sub_categories,
            'materials': materials,
            'selected_categorie_ids': selected_categorie_ids,  # Passer les IDs des catégories sélectionnées
            'selected_Sous_categorie_ids': selected_Sous_categorie_ids,  # Passer les IDs des sous-catégories sélectionnées
            'search_query': query
        }
        
        if(request.user.role  == 'ADMIN'):
            return render(request, 'materiels.html', context)
        else:
            return render(request, 'materiels_user.html', context)

    
    if(request.user.role  == 'ADMIN'):
        return render(request, 'materiels.html', context)
    else:
        return render(request, 'materiels_user.html', context)



def is_admin(user):
    return user.role == 'ADMIN'

def is_user(user):
    return user.role == 'USER'

@method_decorator(login_required, name='dispatch')
class MaterielListView(View):
    def get(self, request):
        category_id = request.GET.get('category_id')
        
        # Charger les catégories
        categories_filter = Categorie.objects.all()
        
        if category_id:
            categories = Categorie.objects.filter(idCategory=category_id)
        else:
            categories = categories_filter
        
        # Charger les autres filtres
        fournisseurs = Fournisseur.objects.all()
        # Charger les autres filtres (sub_categories, form, etc.)
        
        # Préparer les données JSON pour les filtres
        categories_json = [{'id': category.idCategory, 'nom': category.nomCategory} for category in categories]
        # Préparer les autres données JSON pour les filtres (sub_categories_json, etc.)

        # Créer le formulaire
        form = MaterielForm()

        context = {
            'categories_filter': categories_filter,
            'categories': categories,
            # Ajouter d'autres filtres à context (sub_categories, form, etc.)
            'categories_json': json.dumps(categories_json),
            # Ajouter d'autres données JSON pour les filtres (sub_categories_json, etc.)
            'fournisseurs': fournisseurs,
            'selected_category_id': category_id  # Ajout de l'ID de la catégorie sélectionnée au contexte
        }
        
        if(request.user.role  == 'ADMIN'):
            return render(request, 'materiels.html', context)
        else:
            return render(request, 'materiels_user.html', context)
            



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

def get_sous_categories_for_categorie(request, categorie_id):
    try:
        categories = Categorie.objects.values('idCategory', 'nomCategory')
        selected_categorie = Categorie.objects.get(idCategory=categorie_id)
        selected_categorie_ids = [selected_categorie.idCategory]  # Créer une liste d'IDs de catégories

        sub_categories = selected_categorie.souscategorie_set.all()
        fournisseurs = Fournisseur.objects.all()


        category_id = request.GET.get('category_id')
        # Charger les catégories
        categories_filter = Categorie.objects.all()
        if category_id:
            categories = Categorie.objects.filter(idCategory=category_id)
        else:
            categories = categories_filter
        # Charger les autres filtres
        fournisseurs = Fournisseur.objects.all()
        context = {
            'categories': categories,
            'selected_categorie': selected_categorie,
            'sub_categories': sub_categories,
            'categories_filter': categories_filter,
            'selected_categorie_ids':selected_categorie_ids,
            'fournisseurs': fournisseurs,

            'selected_category_id': category_id  # Ajout de l'ID de la catégorie sélectionnée au contexte

        }

        
        if(request.user.role  == 'ADMIN'):
            return render(request, 'materiels.html', context)
        else:
            return render(request, 'materiels_user.html', context)
        
    except Categorie.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)




def get_materials_for_subcategory(request, category_id, subcategory_id):
    try:
        # Récupération des catégories et sous-catégories
        categories = Categorie.objects.values('idCategory', 'nomCategory')
        selected_categorie = Categorie.objects.get(idCategory=category_id)
        sub_categories = selected_categorie.souscategorie_set.all()
        selected_subcategorie = SousCategorie.objects.get(idSousCategorie=subcategory_id)
        fournisseurs = Fournisseur.objects.all()

        selected_categorie_ids = [selected_categorie.idCategory]  
        selected_Sous_categorie_ids = [selected_subcategorie.idSousCategorie ]  
        # Récupération des matériaux pour la sous-catégorie sélectionnée
        materials_list = selected_subcategorie.materiel_set.all()

        # Pagination
        page = request.GET.get('page', 1)  # Récupère le numéro de page de la requête, sinon utilise 1 par défaut
        paginator = Paginator(materials_list, 4)  # 10 matériaux par page
        materials = paginator.get_page(page)

        context = {
            'categories': categories,
            'sub_categories': sub_categories,
            'selected_categorie': selected_categorie,
            'selected_Sous_categorie': selected_subcategorie,
            'selected_categorie_ids':selected_categorie_ids,
            'selected_Sous_categorie_ids':selected_Sous_categorie_ids,
            'fournisseurs': fournisseurs,
            'materials': materials
        }

        
        if(request.user.role  == 'ADMIN'):
            return render(request, 'materiels.html', context)
        else:
            return render(request, 'materiels_user.html', context)
        
    except SousCategorie.DoesNotExist:
        return JsonResponse({'error': 'SousCategorie not found'}, status=404)




@login_required
@user_passes_test(is_admin)
def delete_materiel(request, materiel_id):
    materiel = get_object_or_404(Materiel, idMateriel=materiel_id)
    materiel_name = materiel.nomMateriel  # Get the name before deleting the object
    materiel.delete()
    messages.success(request, f"Le matériel {materiel_name} a été supprimé.")
    return redirect(reverse('materiel_list'))

@login_required
@user_passes_test(is_admin)
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


