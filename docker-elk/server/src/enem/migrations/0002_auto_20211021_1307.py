# Generated by Django 3.2.8 on 2021-10-21 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enem', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidato',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='municipio',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='prova',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='realiza',
            options={'managed': False},
        ),
    ]
