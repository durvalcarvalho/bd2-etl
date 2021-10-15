from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Municipio(models.Model):
    codMunicipio = models.IntegerField(primary_key=True)
    nomeMunicipio = models.CharField(max_length=200)
    siglaUf = models.CharField(max_length=4)


class Candidato(models.Model):
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

    codMunicipio = models.ForeignKey(
        to=Municipio,
        on_delete=models.CASCADE,
        related_name='candidatos',
    )


class Prova(models.Model):

    class CorProvaChoices(models.IntegerChoices):
        AZUL = (507, "Azul")
        AMARELA = (508, "Amarela")
        BRANCA = (509, "Branca")
        ROSA = (510, "Rosa")
        LARANJA_ADAPTADA_LEDOR = (520, "Laranja - Adaptada Ledor")
        VERDE_VIDEOPROVA_LIBRAS = (524, "Verde - Videoprova - Libras")
        AZUL_REAPLICACAO = (547, "Azul (Reaplicação)")
        AMARELO_REAPLICACAO = (548, "Amarelo (Reaplicação)")
        BRANCO_REAPLICACAO = (549, "Branco (Reaplicação)")
        ROSA_REAPLICACAO = (550, "Rosa (Reaplicação)")
        LARANJA_ADAPTADA_LEDOR_REAPLICACAO = (
            564,
            "Laranja - Adaptada Ledor (Reaplicação)"
        )

    idProva = models.IntegerField(primary_key=True)
    corCiencias = models.IntegerField(choices=CorProvaChoices)
    corMatematica = models.IntegerField(choices=CorProvaChoices)
    corHumanas = models.IntegerField(choices=CorProvaChoices)
    corLinguagem = models.IntegerField(choices=CorProvaChoices)


class Realiza(models.Model):

    idResultado = models.IntegerField(primary_key=True)

    idProva = models.ForeignKey(
        to=Prova,
        on_delete=models.CASCADE,
        related_name='realizacoes',
    )

    class StatusChoices(models.IntegerChoices):
        SEM_PROBLEMAS           = (1, "Sem problemas")
        ANULADA                 = (2, "Anulada")
        COPIA_TEXTO_MOTIVADOR   = (3, "Cópia Texto Motivador")
        EM_BRANCO               = (4, "Em Branco")
        FUGA_AO_TEMA            = (6, "Fuga ao tema")
        NAO_ATENDIMENTO_AO_TIPO_TEXTUAL = (7, "Não atendimento ao tipo textual")
        TEXTO_INSUFICIENTE              = (8, "Texto insuficiente")
        PARTE_DESCONECTADA              = (9, "Parte desconectada")


    statusRedacao = models.IntegerField(choices=StatusChoices)

    inscricaoCandidato = models.ForeignKey(
        to=Candidato,
        on_delete=models.CASCADE,
        related_name='realizacoes',
    )

    notaCiencias = models.DecimalField(
        decimal_places=1,
        max_digits=4,
        validators=[MinValueValidator(0), MaxValueValidator(1000)]
    )

    notaMatematica = models.DecimalField(
        decimal_places=1,
        max_digits=4,
        validators=[MinValueValidator(0), MaxValueValidator(1000)]
    )

    notaHumanas = models.DecimalField(
        decimal_places=1,
        max_digits=4,
        validators=[MinValueValidator(0), MaxValueValidator(1000)]
    )

    notaLinguagem = models.DecimalField(
        decimal_places=1,
        max_digits=4,
        validators=[MinValueValidator(0), MaxValueValidator(1000)]
    )

    notaRedacao = models.DecimalField(
        decimal_places=1,
        max_digits=4,
        validators=[MinValueValidator(0), MaxValueValidator(1000)]
    )

    class TreineiroChoices(models.IntegerChoices):
        SIM = (1, "Sim")
        NAO = (0, "Não")

    treineiro = models.IntegerField(choices=TreineiroChoices)
