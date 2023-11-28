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
        
class FootballFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FootballField
        fields = '__all__'

class FootballFieldImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FootballFieldImage
        fields = '__all__'