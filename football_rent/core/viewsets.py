from pstats import Stats
from rest_framework import viewsets
from core import serializers, models, actions, validate_serializers
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer

    @action(detail=False, methods=['POST'])
    def register(self,request):
        serializer = validate_serializers.Usuario_serializer_validate(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            response = actions.UsuarioActions.save_type(data)
            return Response({"Response":serializer.data})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['GET'])
    def login(self,request):
        pass
    
    @action(detail=True, methods=['POST'])
    def logout(self,request):
        pass