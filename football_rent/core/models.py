from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
import datetime

class ModelBase(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
      

class FootballField(ModelBase):
    name = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        db_column=_('name')
    )
    description = models.CharField(
        max_length=144,
        null=True,
        blank=True,
        db_column= _('description')
    )
    class Meta:
        verbose_name = _("Football field")
        verbose_name_plural = _("Football field")
        
class FootballFieldImage(ModelBase):
    footfield = models.ForeignKey(
        to=FootballField,
        on_delete=models.CASCADE,
        db_index=False,
        null=False,
        db_column= _('football_field_id')
    )
    image = models.BinaryField(
        blank=True,
        null=True,
        db_column= _('binary_image')
    )
    class Meta:
        verbose_name = _("Football field Image")
        verbose_name_plural = _("Football field Image")
        

class Reserva(ModelBase):
    user = models.ForeignKey(
        to=User,
        db_column= _('user_id'),
        db_index=False,
        null=False,
        on_delete=models.DO_NOTHING  
    )
    date = models.DateField(
        db_column= _('date_dt'),
        blank=False,
        null=False
    )
    time = models.TimeField(
        db_column= _('time_dt'),
        blank=False,
        null=False,
        default= datetime.datetime.now()
    )
    football_field = models.ForeignKey(
        to=FootballField,
        db_index=False,
        null=False,
        on_delete=models.DO_NOTHING, 
        db_column=_('football_field_id')
    )

    class Meta:
        verbose_name = _("Reserva")
        verbose_name_plural = _("Reservas")

class Payment(ModelBase):
    reserva = models.ForeignKey(
        to=Reserva,
        db_column= _('reserva_id'),
        db_index=False,
        null=False,
        on_delete=models.DO_NOTHING  
    )
    is_paid = models.BooleanField(
        db_index=False,
        null=False,
        db_column=_('is_paid'),
        default= False,
    )
    
    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payment")
    