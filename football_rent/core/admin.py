from django.contrib import admin
from core import models
# Register your models here.

admin.site.register(models.Reserva)
admin.site.register(models.Payment)
admin.site.register(models.FootballField)
admin.site.register(models.FootballFieldImage)