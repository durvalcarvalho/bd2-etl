import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from enem.models import Municipio, Candidato, Prova, Realiza

data_file='scripts/main.csv'

data = []

with open(data_file, "r") as input_file:
    rows = []
    for row in input_file:
        rows.append(row.strip().split(";"))
    keys = rows[0]

    for values in rows[1:]:
        data.append( dict(zip(keys, values)) )


for row in data:
    prova, created = Prova.objects.get_or_create(
        corNatureza=row["CO_PROVA_CN"],
        corHumanas=row["CO_PROVA_CH"],
        corLinguagem=row["CO_PROVA_LC"],
        corMatematica=row["CO_PROVA_MT"],
    )

    municipio, created = Municipio.objects.get_or_create(
        siglaUf=row["SG_UF_RESIDENCIA"],
        nomeMunicipio=row["NO_MUNICIPIO_RESIDENCIA"],
    )

    participante, created = Candidato.objects.get_or_create(
        inscricao=row["NU_INSCRICAO"],
        sexo=row["TP_SEXO"],
        idade=row["NU_IDADE"],
        cor=row["TP_COR_RACA"],
        codMunicipio=municipio,
    )

    realiza, created = Realiza.objects.get_or_create(
        idProva=prova,
        statusRedacao=row["TP_STATUS_REDACAO"],
        inscricaoCandidato=participante,
        notaNatureza = row["NU_NOTA_CN"],
        notaHumanas = row["NU_NOTA_CH"],
        notaLinguagem = row["NU_NOTA_LC"],
        notaMatematica = row["NU_NOTA_MT"],
        notaRedacao=row["NU_NOTA_REDACAO"],
        treineiro=row["IN_TREINEIRO"],
    )


