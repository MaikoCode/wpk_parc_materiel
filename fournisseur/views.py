from django.shortcuts import render, redirect
from .models import Fournisseur
from .forms import FournisseurForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# @login_required
def fournisseurs_page(request):
    if request.method == "POST":
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fournisseurs')
    else:
        form = FournisseurForm()

    fournisseurs = Fournisseur.objects.all()
    return render(request, 'fournisseur.html', {'fournisseurs': fournisseurs, 'form': form})

@login_required
def delete_fournisseur(request, fournisseurs_id):
    fournisseur = Fournisseur.objects.get(idFournisseur=fournisseurs_id)
    fournisseur.delete()
    messages.success(request, "Le fournisseur " + fournisseur.nomFournisseur +" a été supprimé")
    return redirect('fournisseurs')



@login_required
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






# @login_required
# def fournisseur_new(request):
#     if request.method == "POST":
#         form = FournisseurForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('fournisseurs')
#     else:
#         form = FournisseurForm()
#     return render(request, 'fournisseur/fournisseur_new.html', {'form': form})



# @login_required
# def fournisseur_edit(request, idFournisseur):
#     fournisseur = Fournisseur.objects.all.get(Fournisseur, idFournisseur=idFournisseur)
#     if request.method == "POST":
#         form = FournisseurForm(request.POST, instance=fournisseur)
#         if form.is_valid():
#             form.save()
#             return redirect('fournisseur_list')
#     else:
#         form = FournisseurForm(instance=fournisseur)
#     return render(request, 'fournisseur/fournisseur_edit.html', {'form': form})

# @login_required
# def fournisseur_delete(request, idFournisseur):
#     fournisseur = Fournisseur.objects.all.get(Fournisseur, idFournisseur=idFournisseur)
#     if request.method == 'POST':
#         fournisseur.delete()
#         return redirect('fournisseur_list')
#     return render(request, 'fournisseur/fournisseur_confirm_delete.html', {'fournisseur': fournisseur})




