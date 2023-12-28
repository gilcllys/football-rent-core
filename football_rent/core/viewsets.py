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


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = validate_serializers.UsuarioSerializerValidate(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = behavior.UserBehavior(data=data).run()
        token = Token.objects.get_or_create(user=user[0])
        return Response({
            'token': token[0].pk,
            'user_id': user[0].pk,
            'email': user[0].email,
            'message':user[1]
        })



class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UsuarioSerializer

    @action(detail=False, methods=['POST'])
    def register_employees(self,request):
        serializer = validate_serializers.UsuarioSerializerValidate(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            behavior.UserBehavior(data=data).run()
            return Response({"Response":serializer.data})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['GET'])
    def login(self,request):
        serializer = validate_serializers.LoginSerializerValidate(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            result = behavior.LoginBehavior(data=data).run()
            return Response({"Response":result})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    
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