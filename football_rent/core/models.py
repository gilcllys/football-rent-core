from django.db import models
from django.contrib.auth.models import AbstractUser
from core import managers

class Usuario (AbstractUser):
    id =  models.AutoField(
        primary_key=True, 
        db_column='id'
    )
    full_name = models.CharField(
        null= False,
        blank= False,
        db_column="full_name_txt",
        max_length=124,
        verbose_name= "Full Name"
    )
    email = models.EmailField(
        unique= True,
        null= False,
        blank= False,
        db_column="email_txt",
        verbose_name= "Email"
    )
    is_staff = models.BooleanField(
        null=False,
        blank=False,
        db_column="is_staff_bool",
        verbose_name= "Is Staff"
    )
    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name='Created at'
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified',
        auto_now=True,
        null=True,
        blank=True,
        verbose_name= 'Modified at'
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email','password']
    objects = managers.CustomUserManager()