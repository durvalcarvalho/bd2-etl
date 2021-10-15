CREATE DATABASE IF NOT EXISTS TrabalhoFinal;

USE TrabalhoFinal;

CREATE TABLE MUNICIPIO (
    codMunicipio    INT AUTO_INCREMENT NOT NULL,
    nomeMunicipio   VARCHAR(200)       NOT NULL,
    siglaUf         VARCHAR(4)         NOT NULL,

    CONSTRAINT MUNICIPIO_PK PRIMARY KEY (codMunicipio)
)ENGINE=innoDB AUTO_INCREMENT = 1;

CREATE TABLE CANDIDATO (
    inscricao    INT            NOT NULL,
    sexo         ENUM("M","F")  NOT NULL,
    idade        INT            NOT NULL,

    cor          ENUM("Nao declarado", "Branca", "Preta",
                      "Parda", "Amarela", "Indigena") NOT NULL,

    codMunicipio INT NOT NULL,

    CONSTRAINT CANDIDATO_PK PRIMARY KEY (inscricao),
    CONSTRAINT CANDIDATO_MUNICIPIO_FK FOREIGN KEY (codMunicipio)
            REFERENCES MUNICIPIO (codMunicipio)
)ENGINE=innoDB;

CREATE TABLE PROVA (
    idProva         INT AUTO_INCREMENT NOT NULL,

    corCiencias     ENUM("Azul", "Amarela", "Rosa","Cinza" ,"Laranja - Adaptada Ledor ",
                         "Verde - Videoprova - Libras", "Amarela (Reaplicacao)",
                         "Cinza (Reaplicacao)", "Azul (Reaplicacao)", "Rosa (Reaplicacao)") NOT NULL,

    corMatematica   ENUM("Azul", "Amarela", "Rosa","Cinza" ,"Laranja - Adaptada Ledor ",
                         "Verde - Videoprova - Libras", "Amarela (Reaplicacao)",
                         "Cinza (Reaplicacao)", "Azul (Reaplicacao)", "Rosa (Reaplicacao)") NOT NULL,

    corHumanas      ENUM("Azul", "Amarela", "Rosa","Cinza" ,"Laranja - Adaptada Ledor ",
                         "Verde - Videoprova - Libras", "Amarela (Reaplicacao)",
                         "Cinza (Reaplicacao)", "Azul (Reaplicacao)", "Rosa (Reaplicacao)") NOT NULL,

    corLinguagem    ENUM("Azul", "Amarela", "Rosa","Cinza" ,"Laranja - Adaptada Ledor ",
                         "Verde - Videoprova - Libras", "Amarela (Reaplicacao)",
                         "Cinza (Reaplicacao)", "Azul (Reaplicacao)", "Rosa (Reaplicacao )") NOT NULL,

    CONSTRAINT PROVA_PK PRIMARY KEY (idProva)
)ENGINE=innoDB AUTO_INCREMENT = 1;


CREATE TABLE realiza (
    idProva             INT AUTO_INCREMENT NOT NULL,
    inscricaoCandidato  INT                NOT NULL,

    idResultado         INT                NOT NULL,

    notaCiencias        INT                NOT NULL,
    notaMatematica      INT                NOT NULL,
    notaHumanas         INT                NOT NULL,
    notaLinguagem       INT                NOT NULL,
    statusRedacao ENUM("Sem problemas", "Anulada", "Copia Texto Motivador", "Em Branco",
                       "Fuga ao tema", "Nao atendimento ao tipo textual",
                       "Texto insuficiente", "Parte desconectada") NOT NULL,
    notaRedacao INT                 NOT NULL,
    treineiro   ENUM("SIM","NAO")   NOT NULL,

    CONSTRAINT realiza_PK PRIMARY KEY (idResultado),

    CONSTRAINT realiza_PROVA_FK FOREIGN KEY (idProva)
        REFERENCES PROVA (idProva),

    CONSTRAINT realiza_CANDIDATO_FK FOREIGN KEY (InscricaoCandidato)
        REFERENCES CANDIDATO (inscricao)
)ENGINE=innoDB AUTO_INCREMENT = 1;
