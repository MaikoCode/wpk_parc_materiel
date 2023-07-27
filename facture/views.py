from django.shortcuts import render, redirect
from django.http import HttpResponse
from facture.models import Facture, LigneFacture, Article
from django.contrib import messages

from fournisseur.models import Fournisseur

from django.core.paginator import Paginator

from materiels.models import Materiel

# Create your views here.

def home(request):
    if request.method == "POST":
        # extract fields from the POST request
        date_facture = request.POST.get("date_facture")
        numero_facture = request.POST.get("numero_facture")
        ville = request.POST.get("ville")
        montant_total = request.POST.get("montant_total")

        #check if numero_facture is already in the db (must be unique)
        if Facture.objects.filter(numero_facture=numero_facture).exists():
            messages.error(request, 'Veuillez choisir un autre numéro de facture')
            fournisseurs = Fournisseur.objects.all()
            return render(request, 'facture.html', {'fournisseurs': fournisseurs})

        # create and save Facture instance
        facture = Facture.objects.create(
            date_facture=date_facture,
            numero_facture=numero_facture,
            ville=ville,
            montant_total=montant_total,
            facture_pdf=request.FILES['facture_pdf'] if 'facture_pdf' in request.FILES else None
        )
        # facture.save()
        print('facture num: ', facture.numero_facture)
        print('facture ville: ', facture.ville)
        print('montant total: ',montant_total)

        # extract article ids and quantities
        article_ids = request.POST.getlist("articles")
        quantities = request.POST.getlist("qty")
        prix_unitaires = request.POST.getlist("rate")
        article_ids.pop(0)
        quantities.pop(0)
        prix_unitaires.pop(0)
        print('articles: ', article_ids)
        print('quantities: ', quantities)
        print('les prix unitaire: ', prix_unitaires)



        # # create and save LigneFacture instances
        # for article_name, quantity in zip(article_names, quantities):
        #     ligne_facture = LigneFacture(
        #         facture=facture,
        #         article_id=article_id,
        #         quantite=quantity,
        #     )
        #     # ligne_facture.save()
        # messages.success(request, "Facture ajouté avec succes")
        # # redirect to some page, e.g., the detail view of the created Facture
        # return redirect('facture')
        # Create and save the LigneFacture instances (articles) related to the Facture
        for article_id, quantity, prix_unitaire in zip(article_ids, quantities, prix_unitaires):
            # Get or create the article
            article, created = Article.objects.get_or_create(   
                materiel=Materiel.objects.get(idMateriel=article_id),
                defaults={"prix_unitaire": prix_unitaire}
            )
            sous_total = int(quantity) * float(prix_unitaire)
            LigneFacture.objects.create(
                facture=facture,
                article=article,
                quantite=quantity,
                sous_total=sous_total
            )
        messages.success(request, "Facture ajouté avec succes")
        return redirect('facture')
    else:
        # handle GET request, e.g., by rendering a form
        fournisseurs = Fournisseur.objects.all()
        materiels = Materiel.objects.all()
        return render(request, 'facture.html', {'fournisseurs': fournisseurs, 'materiels':materiels})
    
# def displayfacture(request):
#     factures = Facture.objects.all()
#     return render(request, 'facture_list.html', {'factures': factures})
def displayfacture(request):
    factures_list = Facture.objects.all()
    paginator = Paginator(factures_list, 3) # Show 10 factures per page.
    page_number = request.GET.get('page')
    factures = paginator.get_page(page_number)
    titles = ["Date","Numero","Ville","Montant Total","Details", "Facture PDF"]
    titles2=["Fournisseur","Matériel","Prix","Quantité","Sous-Total"]
    return render(request, 'facture_list.html', {'factures': factures, 'titles': titles, 'titles2': titles2})
