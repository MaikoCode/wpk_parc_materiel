from django.shortcuts import render, redirect,get_object_or_404
from materiels.models import Materiel
from .models import Maintenance
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import NoteForm
def maintenances(request):
    if request.method == "POST":
        materiel_id = request.POST.get('materiel')
        file = request.FILES.get('file') if 'file' in request.FILES else None
        materiel = Materiel.objects.get(pk=materiel_id)
        description = request.POST.get('description')
        maintenance = Maintenance(materiel=materiel, file=file, description=description)
        maintenance.save()
        messages.success(request, 'Maintenance ajouté.')
        return redirect('maintenance')  # Redirect to a relevant page after saving

    materiels = Materiel.objects.all()
    maintenances = Maintenance.objects.all().order_by('-date_panne')
    page = Paginator(maintenances, 4)
    page_liste = request.GET.get('page')
    maintenances = page.get_page(page_liste) 
    context = {'materiels': materiels, 'maintenances':maintenances}
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
            messages.success(request, 'Note added successfully.')
            return redirect('detail_maintenance', maintenace_id=maintenance.id)
        else:
            messages.error(request, 'une erreur rencontré lors de l envoie du form')
    return render(request, 'detail_maintenance.html', {'maintenance':maintenance, 'form2': form2})