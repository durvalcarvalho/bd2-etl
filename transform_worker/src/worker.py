import os
import sys
import ftfy
import signal
import logging
import requests
from time import sleep


import json

from kafka import KafkaConsumer, KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError, NoBrokersAvailable
from kafka.consumer.fetcher import ConsumerRecord

logger = logging.getLogger('kafka')
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.ERROR)


settings = {
    "GROUP_ID": "transform_worker_2",
    "KAFKA_BROKER_SERVERS": "kafka:9092",
    "TOPICS": (
        'mysql-server.django_enem.enem_realiza',
    )
}

consumer = KafkaConsumer(
    group_id=settings["GROUP_ID"],
    bootstrap_servers=settings["KAFKA_BROKER_SERVERS"],
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    # key_deserializer=lambda x: json.loads(x.decode('ISO-8859-1')),
    value_deserializer=lambda x: json.loads(x.decode('ISO-8859-1')),
)

consumer.subscribe(settings["TOPICS"])

producer = KafkaProducer(
    bootstrap_servers=settings["KAFKA_BROKER_SERVERS"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    # key_serializer=lambda v: json.dumps(v).encode("utf-8"),
)
admin_client = KafkaAdminClient(bootstrap_servers=settings["KAFKA_BROKER_SERVERS"])

def create_topic(topic_name):
    topic_list = [
        NewTopic(name=topic_name, num_partitions=4, replication_factor=1)
    ]
    try:
        admin_client.create_topics(
            new_topics=topic_list,
            validate_only=False,
        )
    except TopicAlreadyExistsError:
        pass


for topic in settings["TOPICS"]:
    create_topic( f"{topic}-transformed" )


IS_SHUTTING_DOWN = False
def graceful_exit(*args, **kwargs):
    global IS_SHUTTING_DOWN
    IS_SHUTTING_DOWN = True

def post_event(event: ConsumerRecord, new_data: dict):
    topic = f"{event.topic}-transformed"
    producer.send(topic=topic, key=event.key, value=new_data)


def get_estado(uf):
    d = {
        'AC': 'Acre',
        'AL': 'Alagoas',
        'AP': 'Amapá',
        'AM': 'Amazonas',
        'BA': 'Bahia',
        'CE': 'Ceará',
        'DF': 'Distrito Federal',
        'ES': 'Espírito Santo',
        'GO': 'Goiás',
        'MA': 'Maranhão',
        'MT': 'Mato Grosso',
        'MS': 'Mato Grosso do Sul',
        'MG': 'Minas Gerais',
        'PA': 'Pará',
        'PB': 'Paraíba',
        'PR': 'Paraná',
        'PE': 'Pernambuco',
        'PI': 'Piauí',
        'RJ': 'Rio de Janeiro',
        'RN': 'Rio Grande do Norte',
        'RS': 'Rio Grande do Sul',
        'RO': 'Rondônia',
        'RR': 'Roraima',
        'SC': 'Santa Catarina',
        'SP': 'São Paulo',
        'SE': 'Sergipe',
        'TO': 'Tocantins'
    }
    try:
        return d[uf]
    except Exception:
        return None

def get_prova_color(color_number):
    d = {
        "1": "Azul",
        "2": "Amarela",
        "3": "Branca",
        "4": "Rosa",
        "5": "Laranja - Adaptada Ledor",
        "6": "Verde - Videoprova - Libras",
        "7": "Azul (Reaplicação)",
        "8": "Amarela (Reaplicação)",
        "9": "Branco (Reaplicação)",
        "10": "Rosa (Reaplicação)",
        "11": "Laranja - Adaptada Ledor (Reaplicação)",
        "12": "Cinza",
        "13": "Cinza (Reaplicação)",
    }
    try:
        return d[color_number]
    except Exception:
        return None

def get_candidato_color(cor_code):
    d = {
        0: "Não declarado",
        1: "Branca",
        2: "Preta",
        3: "Parda",
        4: "Amarela",
        5: "Indígena",
    }
    try:
        return d[cor_code]
    except Exception:
        return None

def get_redacao_result(redacao_code):
    d = {
        "1": "Sem problemas",
        "2": "Anulada",
        "3": "Cópia Texto Motivador",
        "4": "Em Branco",
        "6": "Fuga ao tema",
        "7": "Não atendimento ao tipo textual",
        "8": "Texto insuficiente",
        "9": "Parte desconectada"
    }
    try:
        return d[redacao_code]
    except Exception:
        return None


def process_event(event: ConsumerRecord):
    new_data = event.value['payload']['after']

    key: str
    for key in new_data.keys():
        if key.startswith('nota'):
            try:
                new_data[key] = float( new_data[key] )
            except Exception:
                new_data[key] = None

    idProva = new_data["idProva_id"]
    response = requests.get(f'http://backend:8000/provas/{idProva}')
    prova_content = response.json()

    key: str
    for key in prova_content.keys():
        if key.startswith('cor'):
            prova_content[key] = get_prova_color(prova_content[key])

    new_data.pop("idProva_id")
    prova_content.pop("idProva")
    new_data["prova"] = prova_content

    new_data["statusRedacao"] = get_redacao_result( new_data["statusRedacao"] )

    # ---------------------------------------------------------------------- #

    inscricaoCandidato = new_data["inscricaoCandidato_id"]
    response = requests.get(f'http://backend:8000/candidatos/{inscricaoCandidato}')
    candidato_content = response.json()

    candidato_content["cor"] = get_candidato_color( candidato_content["cor"] )

    codMunicipio = candidato_content["codMunicipio"]
    response = requests.get(f'http://backend:8000/municipios/{codMunicipio}')
    municipio_content = response.json()

    municipio_content["nomeMunicipio"] = ftfy.fix_text( municipio_content["nomeMunicipio"] )
    municipio_content["siglaUf"] = get_estado( municipio_content["siglaUf"] )

    municipio_content.pop("codMunicipio")
    candidato_content.pop("codMunicipio")

    candidato_content["municipio"] = municipio_content

    if candidato_content["sexo"] == "M":
        candidato_content["sexo"] = "MASCULINO"
    elif candidato_content["sexo"] == "F":
        candidato_content["sexo"] = "FEMININO"
    else:
        candidato_content["sexo"] = None

    new_data.pop("inscricaoCandidato_id")

    new_data["candidato"] = candidato_content

    if new_data["treineiro"] == "0":
        new_data["treineiro"] = "Não"
    else:
        new_data["treineiro"] = "Sim"

    # TODO Push to topic
    post_event(event, new_data)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, graceful_exit)
    signal.signal(signal.SIGTERM, graceful_exit)

    while IS_SHUTTING_DOWN == False:
        try:
            event = next(consumer)
            process_event(event)
            consumer.commit()

            print(f"\n\nEvent processed successfully. Key: {event.key}; Value: {event.value}\n\n")

        except StopIteration as err:
            if IS_SHUTTING_DOWN:
                print("The worker terminated gracefully")
                break

    consumer.close()
    sys.exit()