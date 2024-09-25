from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import AbstractUser


# Modelo de Categorias
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome

# Gerenciador de Usuários Customizado
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O usuário deve ter um endereço de e-mail')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuário deve ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuário deve ter is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

# Modelo Customizado de Usuário
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    nome = models.CharField(max_length=30, blank=True)
    sobrenome = models.CharField(max_length=30, blank=True)
    room = models.CharField(max_length=255, blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# Modelo Perfil de Usuário
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    foto_perfil = models.ImageField(upload_to='perfil/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Perfis de Usuários'

    def __str__(self):
        return self.nome

# Modelo de Logs de Acesso
class LogAcesso(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    data_acesso = models.DateTimeField(auto_now_add=True)
    endereco_ip = models.GenericIPAddressField()

    class Meta:
        verbose_name_plural = 'Logs de Acesso'

    def __str__(self):
        return f'{self.usuario.nome} - {self.data_acesso}'

# Modelo de Tutorial
class Tutorial(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    conteudo = models.TextField()
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Tutoriais'

    def __str__(self):
        return self.titulo

# Modelo de Desenho
class Desenho(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    arquivo = models.ImageField(upload_to='desenhos/')
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    data_postagem = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Desenhos'

    def __str__(self):
        return self.titulo

# Modelo de Avaliação
class Avaliacao(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.TextField()
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Avaliações'

    def __str__(self):
        return f'{self.usuario.nome} - {self.tutorial.titulo} - {self.nota}'

# Modelo de Suporte
class Suporte(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('aberto', 'Aberto'), ('em andamento', 'Em andamento'), ('fechado', 'Fechado')], default='aberto')

    class Meta:
        verbose_name_plural = 'Suporte'

    def __str__(self):
        return f'{self.assunto} - {self.status}'

# Modelo de Curtida
class Curtida(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    desenho = models.ForeignKey(Desenho, on_delete=models.CASCADE)
    data_curtida = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Curtidas'

    def __str__(self):
        return f'{self.usuario.nome} - {self.desenho.titulo}'

# Modelo de Comentário
class Comentario(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    desenho = models.ForeignKey(Desenho, on_delete=models.CASCADE)
    texto = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Comentários'

    def __str__(self):
        return f'{self.usuario.nome} - {self.desenho.titulo} - {self.texto[:20]}'

class Usuario(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    data_criacao = models.DateTimeField(auto_now_add=True)
    foto_perfil = models.ImageField(upload_to='perfil/', blank=True, null=True)
    bio = models.TextField(blank=True, default="Sem biografia")
    room = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nome