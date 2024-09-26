from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser  # Certifique-se de que está importando seu modelo CustomUser
from .forms import EditProfileForm, EditUsuarioForm, EditPerfilUsuarioForm  # Importando os formulários
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm 
from .forms import UserUpdateForm 
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from .models import Suporte
from django.contrib.auth.decorators import login_required
from .models import Tutorial

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')



class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password:
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                user = None
            
            if user:
                user = authenticate(request, username=user.email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('index')  # Redireciona para a página principal
                else:
                    messages.error(request, 'Senha incorreta.')
            else:
                messages.error(request, 'Email não encontrado.')
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')
    
        return render(request, 'login.html')

@login_required
def perfil(request):
    user = request.user  # Obtém o usuário atual
    return render(request, 'perfil.html', {'user': user})

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email já existe'})
        
        user = CustomUser.objects.create_user(email=email, password=password)
        user.save()
        login(request, user)  # Faz login automaticamente após o registro
        return redirect('index')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')  # Redireciona para a página de login após logout


@login_required
def perfil_view(request):
    usuario = request.user  # ou obtenha o usuário de outra maneira
    return render(request, 'perfil.html', {'user': usuario})
def editar_perfil(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')  # Redirecionar para a página de perfil após salvar
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'editar_perfil.html', {'form': form})
@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('perfil')  # Certifique-se de que a URL 'perfil' está correta
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'editar_perfil.html', {'form': form})

class SuporteView(View):
    def get(self, request):
        return render(request, 'suporte.html')

    def post(self, request):
        # Lógica para enviar suporte
        pass


class PostarView(View):
    def get(self, request):
        return render(request, 'postar.html')

    def post(self, request):
        # Lógica para postar
        pass



class TutorialView(View):
    def get(self, request):
        tutoriais = Tutorial.objects.all()
        return render(request, 'tutorial.html', {'tutoriais': tutoriais})
class EditarUsuarioView(View):
    @login_required
    def get(self, request):
        user = request.user.usuario
        form = EditUsuarioForm(instance=user)
        return render(request, 'editar_usuario.html', {'form': form})

    @login_required
    def post(self, request):
        user = request.user.usuario
        form = EditUsuarioForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect('perfil')
        return render(request, 'editar_usuario.html', {'form': form})


class EditarPerfilUsuarioView(View):
    @login_required
    def get(self, request):
        perfil = request.user.perfilusuario
        form = EditPerfilUsuarioForm(instance=perfil)
        return render(request, 'editar_perfil_usuario.html', {'form': form})

    @login_required
    def post(self, request):
        perfil = request.user.perfilusuario
        form = EditPerfilUsuarioForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil de usuário atualizado com sucesso!')
            return redirect('perfil')
        return render(request, 'editar_perfil_usuario.html', {'form': form})


@login_required
def suporte_view(request):
    print("Requisição recebida: ", request.method)  # Adicione este print
    if request.method == "POST":
        usuario = request.user
        assunto = request.POST.get('assunto')
        mensagem = request.POST.get('mensagem')
        status = 'Em aberto'  # Definindo um status padrão para a mensagem de suporte

        # Salva o suporte no banco de dados
        Suporte.objects.create(usuario=usuario, assunto=assunto, mensagem=mensagem, status=status)

        # Mensagem de sucesso
        messages.success(request, 'Sua mensagem foi enviada com sucesso!')
        
        # Redireciona para a página de suporte ou para onde você quiser
        return redirect('suporte')  

    print("Renderizando o template suporte.html")  # Adicione este print
    return render(request, 'suporte.html')   