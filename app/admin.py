from django.contrib import admin
from .models import (
    CustomUser,
    Comentario,
    Curtida,
    LogAcesso,
    Tutorial,
    Desenho,
    Avaliacao,
    PerfilUsuario,
    Suporte,
    Categoria
)

# Inline para Comentario
class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 1

# Inline para Curtida
class CurtidaInline(admin.TabularInline):
    model = Curtida
    extra = 1

# Admin para LogAcesso
class LogAcessoAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'data_acesso', 'endereco_ip']
    search_fields = ['usuario__nome', 'endereco_ip']

# Admin para Tutorial
class TutorialAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'data_criacao')  # Certifique-se que 'data_criacao' existe no modelo Tutorial
    search_fields = ['titulo', 'autor__nome', 'categoria']

# Admin para Desenho
class DesenhoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'usuario', 'data_publicacao']  # Corrigido para 'data_publicacao'
    search_fields = ['titulo', 'usuario__nome']
    inlines = [ComentarioInline, CurtidaInline]

# Admin para Avaliacao
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'tutorial', 'usuario', 'nota', 'data_avaliacao']
    search_fields = ['tutorial__titulo', 'usuario__nome']

# Admin para PerfilUsuario
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'foto_perfil']
    search_fields = ['usuario__nome']

# Admin para Suporte
class SuporteAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'assunto', 'status', 'data_criacao']  # Certifique-se de que 'data_criacao' existe no modelo Suporte
    search_fields = ['usuario__nome', 'assunto', 'status']

# Admin para Categoria
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']

# Registro dos modelos no admin
admin.site.register(CustomUser)  # Registre CustomUser se necessário
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(LogAcesso, LogAcessoAdmin)
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Desenho, DesenhoAdmin)
admin.site.register(Avaliacao, AvaliacaoAdmin)
admin.site.register(PerfilUsuario, PerfilUsuarioAdmin)
admin.site.register(Suporte, SuporteAdmin)
admin.site.register(Curtida)
admin.site.register(Comentario)