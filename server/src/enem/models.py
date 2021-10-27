from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Municipio(models.Model):

    codMunicipio = models.AutoField(primary_key=True)
    nomeMunicipio = models.CharField(max_length=200)  # Field name made lowercase.
    siglaUf = models.CharField(max_length=4)  # Field name made lowercase.

    def __str__(self) -> str:
        return f"{self.codMunicipio} - {self.nomeMunicipio} - {self.siglaUf}"

class Candidato(models.Model):
    # class Meta:
    #    managed = False
    #    db_table = 'CANDIDATO'
    inscricao = models.CharField(max_length=12, primary_key=True)

    class SexoChoices(models.TextChoices):
        MASCULINO = ('M', "MASCULINO")
        FEMININO  = ('F', "FEMININO")

    sexo = models.CharField(
        max_length=1,
        choices=SexoChoices.choices,
    )

    idade = models.IntegerField()

    class CorChoices(models.IntegerChoices):
        NAO_DECLARADO = (0, "Não declarado")
        BRANCA        = (1, "Branca")
        PRETA         = (2, "Preta")
        PARDA         = (3, "Parda")
        AMARELA       = (4, "Amarela")
        INDIGENA      = (5, "Indígena")

    cor = models.IntegerField(choices=CorChoices.choices)

    codMunicipio = models.ForeignKey('Municipio', models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.inscricao} - {self.sexo} - {self.idade} - {self.cor} - {self.codMunicipio}"


class Prova(models.Model):
    # class Meta:
    #    managed = False
    #    db_table = 'PROVA'

    class CorProvaChoices(models.IntegerChoices):
        AZUL = (1, "Azul")
        AMARELA = (2, "Amarela")
        BRANCA = (3, "Branca")
        ROSA = (4, "Rosa")
        LARANJA_ADAPTADA_LEDOR = (5, "Laranja - Adaptada Ledor")
        VERDE_VIDEOPROVA_LIBRAS = (6, "Verde - Videoprova - Libras")
        AZUL_REAPLICACAO = (7, "Azul (Reaplicação)")
        AMARELO_REAPLICACAO = (8, "Amarela (Reaplicação)")
        BRANCO_REAPLICACAO = (9, "Branco (Reaplicação)")
        ROSA_REAPLICACAO = (10, "Rosa (Reaplicação)")
        LARANJA_ADAPTADA_LEDOR_REAPLICACAO = (
            11,
            "Laranja - Adaptada Ledor (Reaplicação)"
        )
        CINZA = (12, "Cinza")
        CINZA_REAPLICACAO = (13, "Cinza (Reaplicação)")

    idProva = models.AutoField(primary_key=True)  # Field name made lowercase.

    corNatureza = models.CharField(max_length=2, blank=True, null=True)

    corHumanas = models.CharField(max_length=2, blank=True, null=True)  # Field name made lowercase.

    corLinguagem = models.CharField(max_length=2, blank=True, null=True)  # Field name made lowercase.

    corMatematica = models.CharField(max_length=2, blank=True, null=True)  # Field name made lowercase.

    def __str__(self) -> str:
        return (
            f"{self.idProva} - "
            f"{self.corNatureza} - "
            f"{self.corHumanas} - "
            f"{self.corLinguagem} - "
            f"{self.corMatematica} - "
        )



class Realiza(models.Model):
    # class Meta:
    #    managed = False
    #    db_table = 'realiza'

    idResultado = models.AutoField(primary_key=True)  # Field name made lowercase.

    idProva = models.ForeignKey(Prova, models.DO_NOTHING)  # Field name made lowercase.

    class StatusChoices(models.IntegerChoices):
        SEM_PROBLEMAS           = (1, "Sem problemas")
        ANULADA                 = (2, "Anulada")
        COPIA_TEXTO_MOTIVADOR   = (3, "Cópia Texto Motivador")
        EM_BRANCO               = (4, "Em Branco")
        FUGA_AO_TEMA            = (6, "Fuga ao tema")
        NAO_ATENDIMENTO_AO_TIPO_TEXTUAL = (7, "Não atendimento ao tipo textual")
        TEXTO_INSUFICIENTE              = (8, "Texto insuficiente")
        PARTE_DESCONECTADA              = (9, "Parte desconectada")


    statusRedacao = models.CharField(max_length=1, blank=True, null=True)  # Field name made lowercase.

    inscricaoCandidato = models.ForeignKey(Candidato, models.DO_NOTHING)  # Field name made lowercase.

    notaNatureza = models.CharField(max_length=6, blank=True, null=True)  # Field name made lowercase.

    notaHumanas = models.CharField(max_length=6, blank=True, null=True)  # Field name made lowercase.

    notaMatematica = models.CharField(max_length=6, blank=True, null=True)  # Field name made lowercase.

    notaLinguagem = models.CharField(max_length=6, blank=True, null=True)  # Field name made lowercase.

    notaRedacao = models.CharField(max_length=6, blank=True, null=True)  # Field name made lowercase.

    class TreineiroChoices(models.IntegerChoices):
        SIM = (1, "Sim")
        NAO = (0, "Não")

    treineiro = models.CharField(max_length=1)

    def __str__(self) -> str:
        return (
            f"{self.idResultado} - "
            f"{self.idProva} - "
            f"{self.statusRedacao} - "
            f"{self.inscricaoCandidato} - "
            f"{self.notaNatureza} - "
            f"{self.notaHumanas} - "
            f"{self.notaMatematica} - "
            f"{self.notaLinguagem} - "
            f"{self.notaRedacao} - "
            f"{self.treineiro} - "
        )
