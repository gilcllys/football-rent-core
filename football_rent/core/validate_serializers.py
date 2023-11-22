from rest_framework import serializers
from rest_framework import serializers

class Usuario_serializer_validate(serializers.Serializer):
    email = serializers.EmailField(
        required=True, 
        allow_null=False
    )
    full_name = serializers.CharField(
        required=True, 
        allow_null=False,
        max_length=124,   
    )
    username = serializers.CharField(
        required=True, 
        allow_null=False,
        max_length=124,   
    )
    is_staff = serializers.BooleanField(
        required=True, 
       allow_null=False
    )
    is_staff = serializers.IntegerField(
        required=True, 
        allow_null=False
    )
    mode = serializers.IntegerField(
        required=True, 
        allow_null=False
    )
    password = serializers.CharField(
        required=True, 
        allow_null=False, 
    )