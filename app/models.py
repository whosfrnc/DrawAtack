from django.db import models
from django.contrib.auth.models import User



class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nome


class LogAcesso(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_acesso = models.DateTimeField(auto_now_add=True)
    endereco_ip = models.GenericIPAddressField()

    class Meta:
        verbose_name_plural = 'LogsAcesso'

    def __str__(self):
        return f'{self.usuario.nome} - {self.data_acesso}'


class Tutorial(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    conteudo = models.TextField()
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Tutoriais'

    def __str__(self):
        return self.titulo


class Desenho(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    arquivo = models.ImageField(upload_to='desenhos/')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_postagem = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Desenhos'

    def __str__(self):
        return self.titulo


class Avaliacao(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.TextField()
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Avaliacoes'

    def __str__(self):
        return f'{self.usuario.nome} - {self.tutorial.titulo} - {self.nota}'


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    foto_perfil = models.ImageField(upload_to='perfil/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'PerfilUsuario'

    def __str__(self):
        return self.usuario.nome


class Suporte(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('aberto', 'Aberto'), ('em andamento', 'Em andamento'), ('fechado', 'Fechado')], default='aberto')

    class Meta:
        verbose_name_plural = 'Suporte'

    def __str__(self):
        return f'{self.assunto} - {self.status}'


class Curtida(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    desenho = models.ForeignKey(Desenho, on_delete=models.CASCADE)
    data_curtida = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Curtidas'

    def __str__(self):
        return f'{self.usuario.nome} - {self.desenho.titulo}'


class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    desenho = models.ForeignKey(Desenho, on_delete=models.CASCADE)
    texto = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return f'{self.usuario.nome} - {self.desenho.titulo} - {self.texto[:20]}'
