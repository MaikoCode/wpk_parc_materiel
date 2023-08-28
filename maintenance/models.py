from django.db import models
from materiels.models import Materiel
from django.utils import timezone
from employe.models import Employe

# Create your models here.
class Maintenance(models.Model):
    materiel = models.ForeignKey(Materiel, null=True,on_delete=models.CASCADE)
    date_panne = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=130)
    # file = models.FileField(upload_to='filemaintenance/', null=True, blank=True)
    date_reparation = models.DateTimeField(null=True, blank=True)
    files = models.ManyToManyField('MaintenanceFile', blank=True)

class MaintenanceFile(models.Model):
    file = models.FileField(upload_to='filemaintenance/')
    def str(self):
        return self.file.name

class Notesmaintenance(models.Model):
    maintenance = models.ForeignKey(Maintenance, related_name='notesmaintenance', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employe, on_delete=models.CASCADE)
    response_text = models.TextField()
    response_date = models.DateTimeField(default=timezone.now)
    files = models.ManyToManyField('MaintenanceFile', blank=True)