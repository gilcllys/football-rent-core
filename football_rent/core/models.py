from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

class ModelBase(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        

class Reserva(ModelBase):
    clientes = models.ForeignKey(
        to=User,
        db_column= _('cliente_id'),
        blank=False,
        null=False,
        on_delete=models.DO_NOTHING  
    )
    date = models.DateTimeField(
        db_column= _('date_time_dt'),
        blank=False,
        null=False
    )
    payment = models.BooleanField(
        default=False,
        null=False,
        blank=False,
        db_column=_('payment_bool')
    )

    class Meta:
        verbose_name = _("Reserva")
        verbose_name_plural = _("Reservas")
