# Generated by Django 5.0.7 on 2024-09-25 18:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_avaliacao_options_alter_comentario_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='foto_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_perfil/'),
        ),
        migrations.CreateModel(
            name='SupportMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]