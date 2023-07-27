from django.db import models
from materiels.models import Materiel
from employe.models import Employe
from django.contrib.auth.models import User
from django.conf import settings


class Panne(models.Model):
    # Quand on voudra ajouter une panne dans l'interface utilisatuer on pourra utiliser ce model
    # demandeur = models.ForeignKey(Employe, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    date_panne = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    resolue = models.BooleanField(default=False)

    # On fait un ForeignKey au lieu d'un OneToOneField dans le cas si on veut conserver des historiques
    # On ajoute aussi le champ resolue dans  le cas si on veut conserver un historique des differentes pannes

    def __str__(self):
        return self.materiel.nomMateriel