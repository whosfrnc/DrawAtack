# Generated by Django 5.0.7 on 2024-09-25 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_customuser_foto_perfil_supportmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportmessage',
            name='subject',
            field=models.CharField(max_length=200),
        ),
    ]