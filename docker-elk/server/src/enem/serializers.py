from rest_framework import serializers

from enem.models import Candidato, Municipio, Prova, Realiza


class CandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidato
        fields = '__all__'

    def create(self, validated_data: dict):
        candidato, created = Candidato.objects.get_or_create(**validated_data)
        return candidato


class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'

    def create(self, validated_data: dict):
        municipio, created = Municipio.objects.get_or_create(**validated_data)
        return municipio


class ProvaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prova
        fields = '__all__'

    def create(self, validated_data: dict):
        prova, created = Prova.objects.get_or_create(**validated_data)
        return prova


class RealizaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realiza
        fields = '__all__'

    def create(self, validated_data: dict):
        realiza, created = Realiza.objects.get_or_create(**validated_data)
        return realiza
