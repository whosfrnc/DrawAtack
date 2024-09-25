from django.contrib import admin
from .models import (
    CustomUser,
    Usuario,
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

# Admin para o modelo Usuario
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['email', 'bio', 'room']
    search_fields = ['email', 'bio']

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
    list_display = ['id', 'titulo', 'autor', 'data_criacao']
    search_fields = ['titulo', 'autor__nome']

# Admin para Desenho
class DesenhoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'usuario', 'data_postagem']
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
    list_display = ['id', 'usuario', 'assunto', 'data_criacao', 'status']
    search_fields = ['usuario__nome', 'assunto']

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
