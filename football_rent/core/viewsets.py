from rest_framework import viewsets
from rest_framework.decorators import action
from django.contrib.auth.models import User
from core import models
from core import serializers
from core import behavior, validate_serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class CreateUser(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = validate_serializers.UsuarioSerializerValidate(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        response = behavior.UserBehavior(data=data).run()
        return Response(response)

class LoginAuthToken(ObtainAuthToken):

    def get(self, request, *args, **kwargs):
        serializer = validate_serializers.LoginSerializerValidate(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        reponse = behavior.LoginBehavior(data=data).run()
        return Response(reponse)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UsuarioSerializer
    
    @action(detail=True, methods=['POST'])
    def logout(self,request):
        pass
    
class ReservaViewSet(viewsets.ModelViewSet):
    queryset = models.Reserva.objects.all()
    serializer_class = serializers.ReservaSerializer

class FootballFieldViewSet(viewsets.ModelViewSet):
    queryset = models.FootballField.objects.all()
    serializer_class = serializers.FootballFieldSerializer
    
class FootballFieldImageViewSet(viewsets.ModelViewSet):
    queryset = models.FootballFieldImage.objects.all()
    serializer_class = serializers.FootballFieldImageSerializer