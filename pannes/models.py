from django.db import models
from materiels.models import Materiel

class Panne(models.Model):
    # Quand on voudra ajouter une panne dans l'interface utilisatuer on pourra utiliser ce model
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    date_panne = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    resolue = models.BooleanField(default=False)
    
    # On fait un ForeignKey au lieu d'un OneToOneField dans le cas si on veut conserver des historiques
    # On ajoute aussi le champ resolue dans  le cas si on veut conserver un historique des differentes pannes
    
    def _str_(self):
        return self.materiel.nomMateriel