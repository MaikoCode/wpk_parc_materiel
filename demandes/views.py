from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import TicketForm,DescriptionForm
from .models import Ticket
from .forms import ResponseForm,TicketFilterForm
from django.core.paginator import Paginator
def is_user(user):
    return user.role == 'USER'

@login_required
@user_passes_test(is_user)
def DemandePage(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.request_by = request.user.employe
            ticket.save()  # Enregistrer l'objet Ticket d'abord

            # Ajouter les fichiers téléchargés à l'objet Ticket
            files = request.FILES.getlist('files')
            for file in files:
                ticket.files.create(file=file)

            messages.success(request, 'Un nouveau ticket est ajouté.')
            return redirect('demande_user')
        else:
            messages.error(request, 'Une erreur s\'est produite lors de l\'envoi du formulaire.')
    else:
        ticket_form = TicketForm()

    my_demandes = Ticket.objects.filter(request_by=request.user.employe)

    return render(request, 'demande_user.html', {'ticket_form': ticket_form, 'my_demandes': my_demandes})

def TicketDescription(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    form = DescriptionForm(initial={'description': ticket.description})
    form2 = ResponseForm()#form of add response
    if request.method == 'POST':
        form2 = ResponseForm(request.POST)
        if form2.is_valid():
            response = form2.save(commit=False)
            response.ticket = ticket
            response.employee = request.user.employe  # assuming user is an employee
            response.save()
            messages.success(request, 'Comment added successfully.')
            return redirect('ticket_description', ticket_id=ticket.id)
        else:
            messages.error(request, 'une erreur rencontré lors de l envoie du form')
    return render(request, 'ticket_description.html', {'form': form, 'ticket': ticket, 'form2': form2})

def alltickets(request):
    tickets = Ticket.objects.all() 
    return render(request, 'alltickets.html', {'tickets': tickets})


def detailTicketAdmin(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    form = DescriptionForm(initial={'description': ticket.description})
    form2 = ResponseForm()#form of add response
    if request.method == 'POST':
        form2 = ResponseForm(request.POST)
        if form2.is_valid():
            response = form2.save(commit=False)
            response.ticket = ticket
            response.employee = request.user.employe  # assuming user is an employee
            response.save()
            messages.success(request, 'Comment added successfully.')
            return redirect('detail_ticket_admin', ticket_id=ticket.id)
        else:
            messages.error(request, 'une erreur rencontré lors de l envoie du form')

    return render(request, 'detail_ticket_admin.html', {'form': form, 'ticket': ticket, 'form2': form2})

def change_status(request, ticket_id, status):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.status = status
    ticket.save()
    messages.success(request, 'Status de ticket est modifié')
    return redirect('alltickets') 

def alltickets(request):
    form = TicketFilterForm(request.GET)
    tickets = Ticket.objects.all()
    if form.is_valid():
        employee = form.cleaned_data['employee']
        status = form.cleaned_data['status']
        priority = form.cleaned_data['priority']

        if employee:
            tickets = tickets.filter(request_by=employee)
        if status:
            tickets = tickets.filter(status=status)
        if priority:
            tickets = tickets.filter(priority=priority)
    
    page = Paginator(tickets, 4)
    page_liste = request.GET.get('page')
    tickets = page.get_page(page_liste)
    return render(request, 'alltickets.html', {'tickets': tickets, 'form':form})