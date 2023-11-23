from rest_framework import viewsets
from rest_framework.decorators import action
from django.contrib.auth.models import User
from core import serializers
from core import actions, validate_serializers
from rest_framework.response import Response
from rest_framework import status


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UsuarioSerializer

    @action(detail=False, methods=['POST'])
    def register_employees(self,request):
        serializer = validate_serializers.Usuario_serializer_validate(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            actions.UserActions.create_employee(data)
            return Response({"Response":serializer.data})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    @action(detail=False, methods=['POST'])
    def register_managers(self,request):
        
        pass
    @action(detail=False, methods=['POST'])
    def register_costomers(self,request):
    
        pass
    
    @action(detail=True, methods=['GET'])
    def login(self,request):
        pass
    
    @action(detail=True, methods=['POST'])
    def logout(self,request):
        pass