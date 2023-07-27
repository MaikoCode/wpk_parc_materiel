from django import template
from materiels.models import DemandeMateriel

register = template.Library()

@register.filter
def exist_demande(demandeur_id, materiel_id):
    demande_existe = DemandeMateriel.objects.filter(demandeur_id=demandeur_id, materiel_id=materiel_id).exists()
    return demande_existe


@register.filter
def demande_statut(demandeur_id, materiel_id):
    try:
        demande = DemandeMateriel.objects.get(demandeur_id=demandeur_id, materiel_id=materiel_id)
        return demande.status
    except DemandeMateriel.DoesNotExist:
        return None
