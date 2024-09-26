from django import forms
from .models import CustomUser, Usuario, PerfilUsuario

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['foto_perfil','nome','sobrenome', 'bio', 'email']  # Adicione outros campos conforme necessário
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nome', 'sobrenome', 'foto_perfil']


class EditUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha', 'foto_perfil', 'bio']


class EditPerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['foto_perfil', 'bio', 'nome', 'sobrenome']

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nome', 'bio', 'foto_perfil'] 
        
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nome', 'sobrenome', 'email', 'bio', 'room', 'foto_perfil']
        
