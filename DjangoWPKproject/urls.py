
from django.contrib import admin
from django.urls import path
import authentication.views
import employe.views
import fournisseur.views
from materiels.views import MaterielListView
import materiels.views 
import mouvementmateriels.views
import pannes.views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_page, name='login'),
    path('login', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('home/',  authentication.views.home, name='home'),

    path('employes/',  employe.views.employes, name='employes'),
    #employees crud
    path('employee/<int:employee_id>/delete/', employe.views.delete_employee, name='delete_employee'),
    path('employee/<int:employee_id>/edit/', employe.views.edit_employee, name='edit_employee'),
    path('employee/<int:idEmploye>/history', employe.views.employee_mouvement_history,name='employee_mouvement_history'),

    path('fournisseurs/', fournisseur.views.fournisseurs_page, name="fournisseurs" ),
    path('fournisseurs/<int:fournisseurs_id>/delete/', fournisseur.views.delete_fournisseur, name='delete_fournisseur'),
    path('fournisseurs/<int:fournisseurs_id>/edit/', fournisseur.views.edit_fournisseur, name='edit_fournisseur'),

    path('materiel/', MaterielListView.as_view(), name='materiel_list'),
    path('materiel/<int:materiel_id>/delete/', materiels.views.delete_materiel, name='delete_materiel'),
    path('materiel/<int:materiel_id>/edit/', materiels.views.edit_materiel, name='edit_materiel'),

    #mouvements materiels
    path('mouvements/',mouvementmateriels.views.mouvements, name='mouvements'),
    path('mouvement/<int:idMouvement>/delete/', mouvementmateriels.views.delete_mouvement, name='delete_mouvement'),
    path('mouvement/<int:idMouvement>/edit/',mouvementmateriels.views.edit_mouvement, name='edit_mouvement'),
    
    
    path('pannes/', pannes.views.pannes_page, name="pannes"),
    path('pannes/toggle/<int:panne_id>/', pannes.views.toggle_panne, name='toggle_panne'),
    path('pannes/csv/', pannes.views.download_pannes_csv, name='pannes_csv'),
]
