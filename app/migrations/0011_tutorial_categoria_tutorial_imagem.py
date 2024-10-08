# Generated by Django 5.0.7 on 2024-09-26 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_suporte_options_suporte_data_criacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='categoria',
            field=models.CharField(choices=[('cartoon', 'Cartoon'), ('realista', 'Realista'), ('oriental', 'Oriental'), ('abstrato', 'Abstrato'), ('caricatura', 'Caricatura')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='imagem',
            field=models.ImageField(null=True, upload_to='tutoriais/'),
        ),
    ]
