from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, data):
        if not data['email']:
            raise ValueError("The Email must be set")
        email = self.normalize_email(data['email'])
        user = self.model(
            username=data['username'],
            email=email, 
            full_name=data['full_name'],
            is_staff=data['is_staff']
        )
        user.set_password(data['password'])
        user.save()
        return user

    def create_superuser(self, data):
        if data['is_staff'] is not True:
            raise ValueError("Superuser must have is_staff=True.")
        return self.create_user( 
            username=data['username'],
            email=data['email'], 
            full_name=data['full_name'],
            is_staff=data['is_staff'],
            password=data['password']
        )
