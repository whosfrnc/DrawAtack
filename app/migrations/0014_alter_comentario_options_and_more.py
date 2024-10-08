# Generated by Django 5.0.7 on 2024-09-30 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_usuario_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={},
        ),
        migrations.RenameField(
            model_name='comentario',
            old_name='texto',
            new_name='conteudo',
        ),
        migrations.RenameField(
            model_name='comentario',
            old_name='data_criacao',
            new_name='data_publicacao',
        ),
        migrations.RenameField(
            model_name='comentario',
            old_name='desenho',
            new_name='postagem',
        ),
        migrations.AddField(
            model_name='desenho',
            name='curtidas',
            field=models.IntegerField(default=0),
        ),
    ]
