from django.shortcuts import render, redirect
from django.http import HttpResponse
from facture.models import Facture, LigneFacture, Article
from django.contrib import messages

from fournisseur.models import Fournisseur

# Create your views here.

def home(request):
    if request.method == "POST":
        # extract fields from the POST request
        fournisseur_id = request.POST.get("fournisseur")
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
            fournisseur=Fournisseur.objects.get(idFournisseur=fournisseur_id),
            date_facture=date_facture,
            numero_facture=numero_facture,
            ville=ville,
            montant_total=montant_total
        )
        # facture.save()
        print('facture founis: ',facture.fournisseur.idFournisseur)
        print('facture num: ', facture.numero_facture)
        print('facture ville: ', facture.ville)
        print('montant total: ',montant_total)

        # extract article ids and quantities
        article_names = request.POST.getlist("articles")
        quantities = request.POST.getlist("qty")
        prix_unitaires = request.POST.getlist("rate")
        article_names.pop(0)
        quantities.pop(0)
        prix_unitaires.pop(0)
        print('articles: ', article_names)
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
        for article_name, quantity, prix_unitaire in zip(article_names, quantities, prix_unitaires):
            # Get or create the article
            article, created = Article.objects.get_or_create(
                nom_article=article_name,
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
        return render(request, 'facture.html', {'fournisseurs': fournisseurs})