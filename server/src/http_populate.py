import requests
import sys


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


def process(data_file):
    with open(data_file, "r", encoding='ISO-8859-1') as input_file:

        keys = next(input_file)
        keys = keys.strip().split(";")

        i = 1
        for row in input_file:
            print(f"Processando a linha: {i}")
            i += 1

            row = row.strip().split(";")

            row = dict(zip(keys, row))

            corNatureza = get_color_number(row["CO_PROVA_CN"])
            corHumanas = get_color_number(row["CO_PROVA_CH"])
            corLinguagem = get_color_number(row["CO_PROVA_LC"])
            corMatematica = get_color_number(row["CO_PROVA_MT"])

            url = "http://0.0.0.0:8000/provas/"

            data = {
                "corNatureza": corNatureza,
                "corHumanas": corHumanas,
                "corLinguagem": corLinguagem,
                "corMatematica": corMatematica,
            }

            response = requests.post(url=url, json=data)

            if not response.ok:
                print(response)
                raise Exception("Request Failed")

            data = response.json()
            idProva = data["idProva"]

            # ///////////////////////////////////////////////////////////////// #
            siglaUf=row["SG_UF_RESIDENCIA"]
            nomeMunicipio=row["NO_MUNICIPIO_RESIDENCIA"]

            url = "http://0.0.0.0:8000/municipios/"

            data = { "siglaUf": siglaUf, "nomeMunicipio": nomeMunicipio }

            response = requests.post(url=url, json=data)

            if not response.ok:
                print(response)
                raise Exception("Request Failed")

            data = response.json()
            codMunicipio = data["codMunicipio"]


            # ///////////////////////////////////////////////////////////////// #
            inscricao=row["NU_INSCRICAO"]
            sexo=row["TP_SEXO"]
            idade=row["NU_IDADE"]
            cor=row["TP_COR_RACA"]

            url = "http://0.0.0.0:8000/candidatos/"

            data = {
                "inscricao": inscricao,
                "sexo": sexo,
                "idade": idade,
                "cor": cor,
                "codMunicipio": codMunicipio
            }

            response = requests.post(url=url, json=data)

            if not response.ok:
                print(response)
                raise Exception("Request Failed")

            data = response.json()
            inscricaoCandidato = data["inscricao"]

            # ///////////////////////////////////////////////////////////////// #

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

            url = "http://0.0.0.0:8000/realizas/"

            data = {
                "statusRedacao": statusRedacao,
                "notaNatureza": notaNatureza,
                "notaHumanas": notaHumanas,
                "notaMatematica": notaMatematica,
                "notaLinguagem": notaLinguagem,
                "notaRedacao": notaRedacao,
                "treineiro": treineiro,
                "idProva": idProva,
                "inscricaoCandidato": inscricaoCandidato,
            }

            response = requests.post(url=url, json=data)

            if not response.ok:
                print(response)
                raise Exception("Request Failed")

            data = response.json()


# python3 http_populate.py scripts/files/main_1.csv
if __name__ == "__main__":
    file = sys.argv[1]
    print(f"Processando o arquivo: {file}")
    process(data_file=file)