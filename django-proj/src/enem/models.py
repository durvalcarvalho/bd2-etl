from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Municipio(models.Model):
    codMunicipio = models.AutoField(primary_key=True)
    nomeMunicipio = models.CharField(max_length=200)
    siglaUf = models.CharField(max_length=4)

    def __str__(self) -> str:
        return f"{self.codMunicipio} - {self.nomeMunicipio} - {self.siglaUf}"

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

    def __str__(self) -> str:
        return f"{self.inscricao} - {self.sexo} - {self.idade} - {self.cor} - {self.codMunicipio}"


class Prova(models.Model):

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

    idProva = models.AutoField(primary_key=True)

    corNatureza = models.IntegerField(
        choices=CorProvaChoices.choices,
        null=True,
        blank=True,
    )

    corHumanas = models.IntegerField(
        choices=CorProvaChoices.choices,
        null=True,
        blank=True,
    )

    corLinguagem = models.IntegerField(
        choices=CorProvaChoices.choices,
        null=True,
        blank=True,
    )

    corMatematica = models.IntegerField(
        choices=CorProvaChoices.choices,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return (
            f"{self.idProva} - "
            f"{self.corNatureza} - "
            f"{self.corHumanas} - "
            f"{self.corLinguagem} - "
            f"{self.corMatematica} - "
        )



class Realiza(models.Model):

    idResultado = models.AutoField(primary_key=True)

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


    statusRedacao = models.IntegerField(
        choices=StatusChoices.choices,
        null=True,
        blank=True,
    )

    inscricaoCandidato = models.ForeignKey(
        to=Candidato,
        on_delete=models.CASCADE,
        related_name='realizacoes',
    )

    notaNatureza = models.DecimalField(
        decimal_places=1,
        max_digits=5,
        validators=[MinValueValidator(0), MaxValueValidator(1000)],
        null=True,
        blank=True,
    )

    notaHumanas = models.DecimalField(
        decimal_places=1,
        max_digits=5,
        validators=[MinValueValidator(0), MaxValueValidator(1000)],
        null=True,
        blank=True,
    )

    notaMatematica = models.DecimalField(
        decimal_places=1,
        max_digits=5,
        validators=[MinValueValidator(0), MaxValueValidator(1000)],
        null=True,
        blank=True,
    )

    notaLinguagem = models.DecimalField(
        decimal_places=1,
        max_digits=5,
        validators=[MinValueValidator(0), MaxValueValidator(1000)],
        null=True,
        blank=True,
    )

    notaRedacao = models.DecimalField(
        decimal_places=1,
        max_digits=5,
        validators=[MinValueValidator(0), MaxValueValidator(1000)],
        null=True,
        blank=True,
    )

    class TreineiroChoices(models.IntegerChoices):
        SIM = (1, "Sim")
        NAO = (0, "Não")

    treineiro = models.IntegerField(
        choices=TreineiroChoices.choices,
        null=True,
        blank=True,
    )

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
