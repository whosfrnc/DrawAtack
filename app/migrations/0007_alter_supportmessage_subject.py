# Generated by Django 5.0.7 on 2024-09-25 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_supportmessage_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportmessage',
            name='subject',
            field=models.CharField(max_length=255),
        ),
    ]
