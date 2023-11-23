from rest_framework import serializers
from rest_framework import serializers

class Usuario_serializer_validate(serializers.Serializer):
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