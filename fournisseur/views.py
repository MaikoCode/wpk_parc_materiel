from django.shortcuts import render, redirect
from .models import Fournisseur
from .forms import FournisseurForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.role == 'ADMIN'

@login_required
@user_passes_test(is_admin)
def fournisseurs_page(request):
    query = request.GET.get('search_query')
    if query:
        fournisseurs_list = Fournisseur.objects.filter(Q(nomFournisseur__icontains=query) | Q(adresse__icontains=query) | Q(email__icontains=query) | Q(telephone__icontains=query))
    else:
        fournisseurs_list = Fournisseur.objects.all()
    if request.method == "POST":
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le fournisseur a été ajouté avec succès.")
            return redirect('fournisseurs')
    else:
        form = FournisseurForm()
    paginator = Paginator(fournisseurs_list, 5)
    page_number = request.GET.get('page')
    fournisseurs = paginator.get_page(page_number)
    return render(request, 'fournisseur.html', {'fournisseurs': fournisseurs, 'form': form, 'search_query': query})
    
@login_required
@user_passes_test(is_admin)
def delete_fournisseur(request, fournisseurs_id):
    fournisseur = Fournisseur.objects.get(idFournisseur=fournisseurs_id)
    fournisseur.delete()
    messages.success(request, "Le fournisseur " + fournisseur.nomFournisseur +" a été supprimé")
    return redirect('fournisseurs')

@login_required
@user_passes_test(is_admin)
def edit_fournisseur(request, fournisseurs_id):
    fournisseur = Fournisseur.objects.get(idFournisseur=fournisseurs_id)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            messages.success(request, "Les infos du fournisseur " + fournisseur.nomFournisseur +" ont été modifiés")
            return redirect('fournisseurs')
    else:
        form = FournisseurForm(instance=fournisseur)
    fournisseurs = Fournisseur.objects.all()
    context = {'fournisseurs': fournisseurs, 'form': form}
    return render(request, 'fournisseur.html', context)