from django.contrib import admin
from .models import *

class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 1

class CurtidaInline(admin.TabularInline):
    model = Curtida
    extra = 1

# Customizando a interface de administração para o model 'Usuario'
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'data_criacao']
    search_fields = ['nome', 'email']

# Customizando a interface de administração para o model 'LogAcesso'
class LogAcessoAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'data_acesso', 'endereco_ip']
    search_fields = ['usuario__nome', 'endereco_ip']

# Customizando a interface de administração para o model 'Tutorial'
class TutorialAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'autor', 'data_criacao']
    search_fields = ['titulo', 'autor__nome']
    inlines = [ComentarioInline, CurtidaInline]

# Customizando a interface de administração para o model 'Desenho'
class DesenhoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'usuario', 'data_postagem']
    search_fields = ['titulo', 'usuario__nome']
    inlines = [ComentarioInline, CurtidaInline]

# Customizando a interface de administração para o model 'Avaliacao'
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'tutorial', 'usuario', 'nota', 'data_avaliacao']
    search_fields = ['tutorial__titulo', 'usuario__nome']

# Customizando a interface de administração para o model 'PerfilUsuario'
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'foto_perfil']
    search_fields = ['usuario__nome']

# Customizando a interface de administração para o model 'Suporte'
class SuporteAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'assunto', 'data_criacao', 'status']
    search_fields = ['usuario__nome', 'assunto']

# Customizando a interface de administração para o model 'Categoria'
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']

# Register your models here.
admin.site.register(Categoria),
admin.site.register(Usuario),
admin.site.register(LogAcesso),
admin.site.register(Tutorial),
admin.site.register(Desenho),
admin.site.register(Avaliacao),
admin.site.register(PerfilUsuario),
admin.site.register(Suporte),
admin.site.register(Curtida),
admin.site.register(Comentario),
