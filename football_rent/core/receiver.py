from django.db.models.signals import post_save
from django.dispatch import receiver
from core import models

@receiver(post_save, sender=models.Reserva)
def create_payment(sender, instance, created, **kwargs):
    if created:
        models.Payment.objects.create(reserva_id=instance.id)