from django.shortcuts import render, redirect
from employe.models import Employe
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
from . import forms
from authentication.models import User
from mouvementmateriels.models import MouvementMateriel
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your views here.
def employes(request):
    if request.method == 'POST':
        formEmpData = forms.EmployeForm(request.POST)
        if formEmpData.is_valid():
            print('Valid')
            # employe_name = formEmpData.cleaned_data['nom']
            # print("Employee Name:", employe_name)
            employee = Employe(
                nom=formEmpData.cleaned_data['nom'],
                prenom=formEmpData.cleaned_data['prenom'],
                poste=formEmpData.cleaned_data['poste'],
                dateEmbauche=formEmpData.cleaned_data['dateEmbauche'],
                email=formEmpData.cleaned_data['email']
            )
            employee.save()
            messages.success(request, 'Un nouveau employé est ajouté.')
            return redirect('employes')
    formEmp = forms.EmployeForm()
    # employes = Employe.objects.all()  
    # Handle search query
    search_query = request.GET.get('search_query')
    employes = get_filtered_employes(search_query)
    # = Employe.objects.order_by('idEmploye').all()
    page = Paginator(employes, 2)
    page_liste = request.GET.get('page')
    page = page.get_page(page_liste)  
    return render(request, 'index.html', {'page': page, 'formEmp': formEmp}) 
    # return render(request, 'index.html', {'employes': employes, 'formEmp': formEmp}) 

# Définition de la fonction qui sera exécutée lorsqu'un employé est enregistré
@receiver(post_save, sender=Employe)
def create_user_for_employe(sender, instance, created, **kwargs):
    if created:
        # Utilisez le nom de l'employé comme mot de passe par défaut
        username = instance.email
        password = instance.nom
        user = User.objects.create(username=username, role=User.ADMIN, employe=instance)
        user.set_password(password)  # Définir le mot de passe pour le nouvel utilisateur
        user.save()


def delete_employee(request, employee_id):
    employee = Employe.objects.get(idEmploye=employee_id)
    employee.delete()
    messages.success(request, "L'employé " + employee.nom +" a été supprimé")
    return redirect('employes')

def edit_employee(request, employee_id):
    employee = Employe.objects.get(idEmploye=employee_id)
    print(employee.nom)
    if request.method == 'POST':
        form = forms.EmployeForm(request.POST)
        if form.is_valid():
            # Update the employee details
            employee.nom = form.cleaned_data['nom']
            employee.prenom = form.cleaned_data['prenom']
            employee.dateEmbauche = form.cleaned_data['dateEmbauche']
            employee.poste = form.cleaned_data['poste']
            employee.email = form.cleaned_data['email']
            employee.save()
            print("Le nom modifie ", form.cleaned_data['nom'])
            messages.success(request, "Les infos de l'employé " + employee.nom +" sont modifiés")
    return redirect('employes')



def get_filtered_employes(search_query):
    if search_query:
        return Employe.objects.filter(
            Q(nom__icontains=search_query) |
            Q(prenom__icontains=search_query) |
            Q(dateEmbauche__icontains=search_query) |
            Q(poste__icontains=search_query) |
            Q(email__icontains=search_query)
        ).order_by('idEmploye')
    else:
        return Employe.objects.all().order_by('idEmploye')


def employee_mouvement_history(request, idEmploye):
    employe = Employe.objects.get(idEmploye=idEmploye)
    mouvements = MouvementMateriel.objects.filter(employe=employe)
    return render(request, 'historique_employe.html', {'employe': employe, 'mouvements': mouvements })