from django.contrib.auth.models import User, Group
from django.utils.translation import gettext as _
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from django.db.models import Q

class UserBehavior():
    def __init__(self, data):
        self.data = data
                
    def  create_user(self) -> User:
        try:
            if self.data.get("group") in ['Clientes']:
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
            return self.add_user_to_group(user)
        except Exception as e:
            return e
    
    def  add_user_to_group(self, created_user: User) -> User:
        try:
            group = Group.objects.get(name=self.data.get("group"))
            created_user.groups.add(group)
            return created_user
        except Exception as e:
            return e
        
    def create_token(self, user: User):
        try:
            token, created = Token.objects.get_or_create(user=user)
            return token.key
        except Exception as e:
            return e
        
    def verifyUserExistence(self):
        return User.objects.filter(
            Q(username=self.data.get('username')) | Q( email= self.data.get('email')),
        ).first()


    def run(self):
        if self.verifyUserExistence():
            return {
            "response": "Já existe uma conta com esses dados"
            }
        else:
            user : User = self.create_user()
            return {
                "response": "Salvo com sucesso",
                "contente" : {
                    "user" : user.username,
                    "token": self.create_token(user)
                }
            }

class LoginBehavior():
    def __init__(self, data):
        self.data = data
        self.user = self.verifyUserExistence()
        
    def verifyUserExistence(self):
        return User.objects.filter(
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
            return {"message": "Essa conta não existe"}