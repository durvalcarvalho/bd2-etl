from django.contrib import admin

from enem.models import Municipio, Candidato, Prova, Realiza

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ("codMunicipio", "nomeMunicipio", "siglaUf")
    # search_fields = ("name",)
    # list_filter = ("proven_veracity",)


@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ("inscricao", "sexo", "idade", "cor", "codMunicipio")
    # search_fields = ("name",)
    # list_filter = ("proven_veracity",)


@admin.register(Prova)
class ProvaAdmin(admin.ModelAdmin):
    list_display = ("idProva", "corNatureza", "corHumanas", "corLinguagem", "corMatematica")
    # search_fields = ("name",)
    # list_filter = ("proven_veracity",)



@admin.register(Realiza)
class RealizaAdmin(admin.ModelAdmin):
    list_display = ("idResultado", "idProva", "statusRedacao", "inscricaoCandidato", "notaNatureza", "notaHumanas", "notaMatematica", "notaLinguagem", "notaRedacao", "treineiro")
    # search_fields = ("name",)
    # list_filter = ("proven_veracity",)
