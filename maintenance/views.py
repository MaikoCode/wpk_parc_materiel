from django.shortcuts import render, redirect, get_object_or_404
from materiels.models import Materiel
from .models import Maintenance, MaintenanceFile
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import NoteForm, DescriptionmaintenanceForm
from datetime import datetime

def maintenances(request):
    if request.method == "POST":
        materiel_id = request.POST.get('materiel')
        materiel = Materiel.objects.get(pk=materiel_id)
        description = request.POST.get('description')
        maintenance = Maintenance(materiel=materiel, description=description)
        maintenance.save()

        files = request.FILES.getlist('files')  # Get all the files
        for file in files:
            maintenance_file = MaintenanceFile(file=file)
            maintenance_file.save()
            maintenance.files.add(maintenance_file)  # Add the file to the maintenance record

        messages.success(request, 'Maintenance ajouté.')
        return redirect('maintenance')

    materiels = Materiel.objects.all()
    maintenances = Maintenance.objects.all().order_by('-date_panne')
    page = Paginator(maintenances, 4)
    page_liste = request.GET.get('page')
    maintenances = page.get_page(page_liste) 
    descform = DescriptionmaintenanceForm()
    context = {'materiels': materiels, 'maintenances':maintenances, 'descform': descform}
    return render(request, 'maintenance.html', context)


def detailMaintenance(request, maintenace_id):
    maintenance = get_object_or_404(Maintenance, id=maintenace_id)
    form2 = NoteForm()#form of add response
    if request.method == 'POST':
        form2 = NoteForm(request.POST)
        if form2.is_valid():
            note = form2.save(commit=False)
            note.maintenance = maintenance
            note.employee = request.user.employe  # assuming user is an employee
            note.save()

            files = request.FILES.getlist('files')  # Get all the files
            for file in files:
                maintenance_file = MaintenanceFile(file=file)
                maintenance_file.save()
                note.files.add(maintenance_file)  # Add the file to the maintenance record

            messages.success(request, 'Note added successfully.')
            return redirect('detail_maintenance', maintenace_id=maintenance.id)
        else:
            messages.error(request, 'une erreur rencontré lors de l envoie du form')
    return render(request, 'detail_maintenance.html', {'maintenance':maintenance, 'form2': form2})


def set_repair_date(request, maintenance_id):
    if request.method == "POST":
        maintenance = get_object_or_404(Maintenance, pk=maintenance_id)
        repair_date = request.POST.get('date_reparation')
        repair_date = datetime.strptime(repair_date, '%Y-%m-%d')
        maintenance.date_reparation = repair_date
        maintenance.save()
        messages.success(request, 'Repair date updated successfully.')
    return redirect('maintenance') # Or wherever you want to redirect

def delete_maintenance(request, maintenance_id):
    maintenance = get_object_or_404(Maintenance, id=maintenance_id)
    maintenance.files.all().delete()
    maintenance.delete()
    messages.success(request, 'Maintenance supprimé.')
    return redirect('maintenance')