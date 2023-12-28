from django.contrib.auth.models import User, Group
from django.utils.translation import gettext as _
from rest_framework.exceptions import AuthenticationFailed

class UserBehavior():
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

class LoginBehavior():
    def __init__(self, data):
        self.data = data
        self.user = self.verifyUserExistence()
        
    def verifyUserExistence(self):
        return User.objects.filter(
            username=self.data.get('username'),
            email= self.data.get('email'),
        ).first()
    
    def getToken(self):
        token = Token.objects.get(user=self.user)
        return token.key
    
    def run(self):
        if(self.verifyUserExistence()):
            return {
                "email": self.user.email,
                "token": self.getToken()
                }
        else:
            return AuthenticationFailed(_("User do not exist"))