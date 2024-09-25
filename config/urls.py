from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from app.views import (
    IndexView,
    LoginView,
    RegisterView,
    LogoutView,
    perfil_view,
    edit_profile_view,
    SuporteView,
    PostarView,
    TutorialView,
    EditarUsuarioView,
    EditarPerfilUsuarioView,
    perfil,
    editar_perfil,
)

urlpatterns = [
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),  # Página inicial
    path('login/', LoginView.as_view(), name='login'),  # Página de login
    path('register/', RegisterView.as_view(), name='register'),  # Página de registro
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout
    path('perfil/', perfil_view, name='perfil'),  # Página de perfil
    path('editar_perfil/', edit_profile_view, name='editar_perfil'),  # Página para editar perfil
    path('suporte/', SuporteView.as_view(), name='suporte'),  # Página de suporte
    path('postar/', PostarView.as_view(), name='postar'),  # Página de postar
    path('tutorial/', TutorialView.as_view(), name='tutorial'),  # Página de tutorial
    path('editar_usuario/', EditarUsuarioView.as_view(), name='editar_usuario'),  # Editar usuário
    path('perfil/', perfil, name='perfil'),
    path('editar_perfil_usuario/', EditarPerfilUsuarioView.as_view(), name='editar_perfil_usuario'),  # Editar perfil do usuário
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
