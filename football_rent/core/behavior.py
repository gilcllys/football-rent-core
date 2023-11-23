from django.contrib.auth.models import User, Group
from django.utils.translation import gettext as _

class UserBeehavior():
    def __init__(self, data):
        self.data = data
    
    def verifyUserExistence(self):
        return User.objects.filter(
            username=self.data.get('username'),
            email= self.data.get('email'),
        ).first()
    
    def  create_general_user(self):
        try:
            if self.data.get("group") in ['Funcionarios','Clientes']:
                user: User =  User.objects.create_user(
                        username=self.data.get('username'),
                        email= self.data.get('email'),
                        password=self.data.get('password')
                    )
            else:
                user: User =  User.objects.create_superuser(
                        username=self.data.get('username'),
                        email= self.data.get('email'),
                        password=self.data.get('password')
                    )
            return user
        except Exception as e:
            return e
    
    def  add_user_to_group(self):
        try:
            user = self.create_general_user()
            group = Group.objects.get(name=self.data.get("group"))
            user.groups.add(group)
            return user
        except Exception as e:
            return e

    def run(self):
        if self.verifyUserExistence():
            return [self.verifyUserExistence(), _("This user already exist")]
        else:
            return [self.add_user_to_group(), _("New user saved")]
       