from rest_framework import viewsets
from rest_framework.decorators import action
from django.contrib.auth.models import User
from core import serializers

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UsuarioSerializer

    @action(detail=False, methods=['POST'])
    def register_employees(self,request):
        
        pass
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