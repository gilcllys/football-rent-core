from django.db import models
from django.utils.translation import gettext as _

class ModelBase(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        

class Reserva(ModelBase):

    

    class Meta:
        verbose_name = _("Reserva")
        verbose_name_plural = _("Reservas")
