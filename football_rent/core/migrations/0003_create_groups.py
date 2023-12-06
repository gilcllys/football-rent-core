# Generated by Django 4.2.6 on 2023-12-06 02:47

from django.db import migrations
from django.contrib.auth.models import Group, Permission

def create_group(apps, schema_editor):
    group_list = ['Funcionarios','Clientes', 'Gerentes']
    for group in group_list:
        new_group = Group(name=group)
        new_group.save()    

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_create_models_reversa_and_footballfieldImage'),
    ]

    operations = [
        migrations.RunPython(create_group),
    ]
