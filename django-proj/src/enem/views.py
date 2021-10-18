from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from rest_framework import status
from rest_framework.response import Response

from enem.models import Candidato, Municipio, Prova, Realiza

from enem.serializers import (
    CandidatoSerializer,
    MunicipioSerializer,
    ProvaSerializer,
    RealizaSerializer,
)

class CandidatoModelViewSet(ModelViewSet):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        data = serializer.data
        codMunicipio = data.get('codMunicipio')
        municipio = Municipio.objects.get(codMunicipio=codMunicipio)
        data["codMunicipio"] = municipio
        candidato, created = Candidato.objects.get_or_create(**data)
        serializer = self.get_serializer(candidato)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class MunicipioModelViewSet(ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

class ProvaModelViewSet(ModelViewSet):
    queryset = Prova.objects.all()
    serializer_class = ProvaSerializer

class RealizaModelViewSet(ModelViewSet):
    queryset = Realiza.objects.all()
    serializer_class = RealizaSerializer
