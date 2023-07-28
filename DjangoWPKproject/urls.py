
from django.contrib import admin
from django.urls import path
import authentication.views
import employe.views
import fournisseur.views
from materiels.views import MaterielListView
from materiels.views import MaterielListView_User
from materiels.views import  Gestion_Demande
import materiels.views
import mouvementmateriels.views
import dashboardAdmin.views
import dashboardUser.views
import pannes.views 
import facture.views
import notification.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_page, name='login'),
    path('login', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('home/',  dashboardAdmin.views.dashboardView, name='home'),
    path('home_user/',  dashboardUser.views.dashboardUserView, name='home_user'),


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
    path('materiels_user/', MaterielListView_User.as_view(), name='materiels_user'),


   #mouvements materiels
    path('mouvements/',mouvementmateriels.views.mouvements, name='mouvements'),
    path('mouvement/<int:idMouvement>/delete/', mouvementmateriels.views.delete_mouvement, name='delete_mouvement'),
    path('mouvement/<int:idMouvement>/edit/',mouvementmateriels.views.edit_mouvement, name='edit_mouvement'),
    path('mouvement/<int:idMouvement>/affect',mouvementmateriels.views.affecter_mouvement,name='affecter_mouvement'),
    

    path('Gestion_Demande',Gestion_Demande.as_view(),name='Gestion_Demande'),


    path('pannes/', pannes.views.pannes_page, name="pannes"),
    path('pannes/toggle/<int:panne_id>/', pannes.views.toggle_panne, name='toggle_panne'),
    path('pannes/csv/', pannes.views.download_pannes_csv, name='pannes_csv'),


    path('demander_materiel/', materiels.views.demander_materiel, name='demander_materiel'),
    path('accepter_demande/<int:demande_id>/', materiels.views.accepter_demande, name='accepter_demande'),
    path('rejeter_demande/<int:demande_id>/', materiels.views.rejeter_demande, name='rejeter_demande'),



    #facture
    path('facture/', facture.views.home, name='facture'),
    path('displayfacture/', facture.views.displayfacture, name='displayfacture'),
    path('read_notification/<int:notification_id>/', notification.views.read_notification, name='read_notification'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
