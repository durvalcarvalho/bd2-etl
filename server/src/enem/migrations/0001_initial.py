# Generated by Django 3.2.8 on 2021-10-28 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('inscricao', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('sexo', models.CharField(choices=[('M', 'MASCULINO'), ('F', 'FEMININO')], max_length=1)),
                ('idade', models.IntegerField()),
                ('cor', models.IntegerField(choices=[(0, 'Não declarado'), (1, 'Branca'), (2, 'Preta'), (3, 'Parda'), (4, 'Amarela'), (5, 'Indígena')])),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('codMunicipio', models.AutoField(primary_key=True, serialize=False)),
                ('nomeMunicipio', models.CharField(max_length=200)),
                ('siglaUf', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Prova',
            fields=[
                ('idProva', models.AutoField(primary_key=True, serialize=False)),
                ('corNatureza', models.CharField(blank=True, max_length=2, null=True)),
                ('corHumanas', models.CharField(blank=True, max_length=2, null=True)),
                ('corLinguagem', models.CharField(blank=True, max_length=2, null=True)),
                ('corMatematica', models.CharField(blank=True, max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Realiza',
            fields=[
                ('idResultado', models.IntegerField(primary_key=True, serialize=False)),
                ('statusRedacao', models.CharField(blank=True, max_length=1, null=True)),
                ('notaNatureza', models.CharField(blank=True, max_length=6, null=True)),
                ('notaHumanas', models.CharField(blank=True, max_length=6, null=True)),
                ('notaMatematica', models.CharField(blank=True, max_length=6, null=True)),
                ('notaLinguagem', models.CharField(blank=True, max_length=6, null=True)),
                ('notaRedacao', models.CharField(blank=True, max_length=6, null=True)),
                ('treineiro', models.CharField(max_length=1)),
                ('idProva', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='enem.prova')),
                ('inscricaoCandidato', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='enem.candidato')),
            ],
        ),
        migrations.AddField(
            model_name='candidato',
            name='codMunicipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='enem.municipio'),
        ),
    ]
