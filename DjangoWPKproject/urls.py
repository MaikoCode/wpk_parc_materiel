from django.contrib import admin
from django.urls import path, include
import authentication.views
import employe.views
import fournisseur.views
from materiels.views import MaterielListView
import materiels.views
import mouvementmateriels.views
import dashboardAdmin.views
import dashboardUser.views
import pannes.views 
import facture.views
import notification.views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
import demandes.views
import maintenance.views
from django.urls import re_path
from django.views.static import serve



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
    path('get_materials_for_subcategory/<int:category_id>/<int:subcategory_id>/', materiels.views.get_materials_for_subcategory, name='get_materials_for_subcategory'),
    path('get_sous_categories_for_categorie/<int:categorie_id>/', materiels.views.get_sous_categories_for_categorie, name='get_sous_categories_for_categorie'),

   #mouvements materiels
    path('mouvements/',mouvementmateriels.views.mouvements, name='mouvements'),
    path('mouvement/<int:idMouvement>/delete/', mouvementmateriels.views.delete_mouvement, name='delete_mouvement'),
    path('mouvement/<int:idMouvement>/edit/',mouvementmateriels.views.edit_mouvement, name='edit_mouvement'),
    path('mouvement/<int:idMouvement>/affect',mouvementmateriels.views.affecter_mouvement,name='affecter_mouvement'),
    



    path('pannes/', pannes.views.pannes_page, name="pannes"),
    path('pannes/toggle/<int:panne_id>/', pannes.views.toggle_panne, name='toggle_panne'),
    path('pannes/csv/', pannes.views.download_pannes_csv, name='pannes_csv'),
    path('pannes_user/', pannes.views.pannes_page_user, name="pannes_user"),


    path('search_materials/', materiels.views.search_materials, name='search_materials'),

    #facture
    path('facture/', facture.views.home, name='facture'),
    path('displayfacture/', facture.views.displayfacture, name='displayfacture'),
    path('read_notification/<int:notification_id>/', notification.views.read_notification, name='read_notification'),
    
    #tickets
    path('demande_user/', demandes.views.DemandePage, name='demande_user'),
    path('summernote/', include('django_summernote.urls')),
    path('ticket_description/<int:ticket_id>/', demandes.views.TicketDescription, name='ticket_description'),
    path('alltickets/',demandes.views.alltickets , name='alltickets' ),
    path('detail_ticket_admin/<int:ticket_id>/', demandes.views.detailTicketAdmin, name="detail_ticket_admin"),
    path('change_status/<int:ticket_id>/<str:status>/', demandes.views.change_status, name='change_status'),
    
    
    #change password
    
    path('change_password/', authentication.views.change_password, name='change_password'),

    #maintenance
    path('maintenance/', maintenance.views.maintenances, name='maintenance'),
    path('detail_maintenance/<int:maintenace_id>/', maintenance.views.detailMaintenance,name="detail_maintenance"),
    path('set_repair_date/<int:maintenance_id>/', maintenance.views.set_repair_date, name='set_repair_date'),
    path('delete_maintenance/<int:maintenance_id>/', maintenance.views.delete_maintenance, name='delete_maintenance'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]

handler404 = 'dashboardAdmin.views.error_404_view'



if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)