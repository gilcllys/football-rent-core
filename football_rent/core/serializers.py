from rest_framework import serializers
from django.contrib.auth.models import User
from core import models

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reserva
        fields = '__all__'