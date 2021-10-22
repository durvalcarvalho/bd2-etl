import os
import django
import jellyfish

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from enem.models import Municipio, Candidato, Prova, Realiza

data_file='scripts/main.csv'



def try_convert_to(convertor, number: str):
    try:
        return convertor(number)
    except ValueError:
        return None

def get_color_number(number: str):
    if not number:
        return None

    number = int(number)

    relation = {503: 1, 504: 2, 505: 12, 506: 4, 519: 5, 523: 6, 543: 8, 544: 13, 545: 7, 546: 10, 507: 1, 508: 2, 509: 3, 510: 4, 520: 5, 524: 6, 547: 7, 548: 8, 549: 9, 550: 10, 564: 11, 511: 1, 512: 2, 513: 4, 514: 3, 521: 5, 525: 6, 551: 7, 552: 8, 553: 9, 554: 10, 565: 11, 515: 1, 516: 2, 517: 4, 518: 12, 522: 5, 526: 6, 555: 8, 556: 13, 557: 7, 558: 10 }

    return relation[number]


with open(data_file, "r", encoding='ISO-8859-1') as input_file:

    keys = next(input_file)
    keys = keys.strip().split(";")

    for row in input_file:
        row = row.strip().split(";")

        row = dict(zip(keys, row))

        corNatureza = get_color_number(row["CO_PROVA_CN"])
        corHumanas = get_color_number(row["CO_PROVA_CH"])
        corLinguagem = get_color_number(row["CO_PROVA_LC"])
        corMatematica = get_color_number(row["CO_PROVA_MT"])

        prova, created = Prova.objects.get_or_create(
            corNatureza=corNatureza,
            corHumanas=corHumanas,
            corLinguagem=corLinguagem,
            corMatematica=corMatematica,
        )
        print(prova)

        siglaUf=row["SG_UF_RESIDENCIA"]
        nomeMunicipio=row["NO_MUNICIPIO_RESIDENCIA"]

        municipio, created = Municipio.objects.get_or_create(
            siglaUf=siglaUf,
            nomeMunicipio=nomeMunicipio,
        )
        print(municipio)

        inscricao=row["NU_INSCRICAO"]
        sexo=row["TP_SEXO"]
        idade=row["NU_IDADE"]
        cor=row["TP_COR_RACA"]

        participante, created = Candidato.objects.get_or_create(
            inscricao=inscricao,
            sexo=sexo,
            idade=idade,
            cor=cor,
            codMunicipio=municipio,
        )
        print(participante)

        statusRedacao = row["TP_STATUS_REDACAO"]

        if not statusRedacao:
            statusRedacao = None

        notaNatureza = try_convert_to(float, row["NU_NOTA_CN"])
        notaHumanas = try_convert_to(float, row["NU_NOTA_CH"])
        notaLinguagem = try_convert_to(float, row["NU_NOTA_LC"])
        notaMatematica = try_convert_to(float, row["NU_NOTA_MT"])
        notaRedacao = try_convert_to(float, row["NU_NOTA_REDACAO"])

        if not row["IN_TREINEIRO"]:
            treineiro = None
        else:
            treineiro = row["IN_TREINEIRO"]

        realiza, created = Realiza.objects.get_or_create(
            idProva=prova,
            inscricaoCandidato=participante,
            statusRedacao=statusRedacao,
            notaNatureza=notaNatureza,
            notaHumanas=notaHumanas,
            notaLinguagem=notaLinguagem,
            notaMatematica=notaMatematica,
            notaRedacao=notaRedacao,
            treineiro=treineiro,
        )
        print(realiza)


