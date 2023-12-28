from rest_framework import serializers
from rest_framework import serializers

class UsuarioSerializerValidate(serializers.Serializer):
    email = serializers.EmailField(
        required=True, 
        allow_null=False
    )
    username = serializers.CharField(
        required=True, 
        allow_null=False,
        max_length=124,   
    )
    password = serializers.CharField(
        required=True, 
        allow_null=False, 
    )
    group = serializers.CharField(
        required=True, 
        allow_null=False, 
    )

class LoginSerializerValidate(serializers.Serializer):
    email = serializers.EmailField(
        required=True, 
        allow_null=False
    )
    password = serializers.CharField(
        required=True, 
        allow_null=False, 
    )