# Generated by Django 5.0.7 on 2024-10-03 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_remove_desenho_curtidas_desenho_curtidas'),
    ]

    operations = [
        migrations.AddField(
            model_name='desenho',
            name='categoria',
            field=models.CharField(choices=[('cartoon', 'Cartoon'), ('realista', 'Realista'), ('oriental', 'Oriental'), ('abstrato', 'Abstrato'), ('caricatura', 'Caricatura')], default='cartoon', max_length=20),
        ),
    ]
