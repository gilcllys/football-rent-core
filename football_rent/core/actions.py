from core import models

class UsuarioActions():
    
    def save_type(data):
        if data['mode'] == 1:
           return models.Usuario.objects.create_superuser(data)
        else:
            return models.Usuario.objects.create_user(data)