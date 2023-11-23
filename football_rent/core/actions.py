from django.contrib.auth.models import User, Group
from django.utils.translation import gettext as _

class UserActions():
    
    def create_custumer(data):
        try:
            group: Group = Group.objects.get(name="Clientes")
            user: User =  User.objects.create_user(
                username=data.get('username'),
                email= data.get('email'),
                password=data.get('password')
            )
            user.groups.add(group)
        except Exception as e:
            return e
        else:
           return _("Your account details have been saved")
       
    def create_employee(data):
        try:
            group: Group = Group.objects.get(name="Funcionarios")
            user: User =  User.objects.create_user(
            username=data.get('username'),
            email= data.get('email'),
            password=data.get('password')
        )
            user.groups.add(group)
        except Exception as e:
            return e
        else:
           return _("Your account details have been saved")   
    
    def create_manager(data):
        try:
            group: Group = Group.objects.get(name="Gerentes")
            user: User =  User.objects.create_user(
            username=data.get('username'),
            email= data.get('email'),
            password=data.get('password')
        )
            user.groups.add(group)
            
        except Exception as e:
            return e
        else:
           return _("Your account details have been saved")
        
       