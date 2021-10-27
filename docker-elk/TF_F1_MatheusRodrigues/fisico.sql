-- CREATE DATABASE IF NOT EXISTS enem;

-- USE enem;

CREATE TABLE MUNICIPIO (
    codMunicipio    INT AUTO_INCREMENT NOT NULL,
    nomeMunicipio   VARCHAR(200)       NOT NULL,
    siglaUf         VARCHAR(4)         NOT NULL,

    CONSTRAINT MUNICIPIO_PK PRIMARY KEY (codMunicipio)
)ENGINE=innoDB AUTO_INCREMENT = 1;


CREATE TABLE CANDIDATO (
    inscricao    VARCHAR(12)    NOT NULL,
    sexo         ENUM("M","F")  NOT NULL,
    idade        INT            NOT NULL,

    cor          ENUM('0','1','2','3','4','5') NOT NULL,

    codMunicipio INT NOT NULL,

    CONSTRAINT CANDIDATO_PK PRIMARY KEY (inscricao),
    CONSTRAINT CANDIDATO_MUNICIPIO_FK FOREIGN KEY (codMunicipio)
            REFERENCES MUNICIPIO (codMunicipio)
)ENGINE=innoDB;


CREATE TABLE PROVA (
    idProva         INT AUTO_INCREMENT NOT NULL,
    corCiencias     ENUM('1','2','3','4','5','6','7','8','9','10','11','12','13'),
    corMatematica   ENUM('1','2','3','4','5','6','7','8','9','10','11','12','13'),
    corHumanas      ENUM('1','2','3','4','5','6','7','8','9','10','11','12','13'),
    corLinguagem    ENUM('1','2','3','4','5','6','7','8','9','10','11','12','13'),

    CONSTRAINT PROVA_PK PRIMARY KEY (idProva)
)ENGINE=innoDB AUTO_INCREMENT = 1;


CREATE TABLE realiza (
    idProva             INT AUTO_INCREMENT NOT NULL,
    inscricaoCandidato  VARCHAR(12)        NOT NULL,

    idResultado         INT                NOT NULL,
    notaCiencias        VARCHAR(6),
    notaMatematica      VARCHAR(6),
    notaHumanas         VARCHAR(6),
    notaLinguagem       VARCHAR(6),


    statusRedacao       ENUM('1','2','3','4','6','7','8','9'),

    notaRedacao         VARCHAR(6),
    treineiro           ENUM('0','1')       NOT NULL,

    CONSTRAINT realiza_PK PRIMARY KEY (idResultado),

    CONSTRAINT realiza_PROVA_FK FOREIGN KEY (idProva)
        REFERENCES PROVA (idProva),

    CONSTRAINT realiza_CANDIDATO_FK FOREIGN KEY (InscricaoCandidato)
        REFERENCES CANDIDATO (inscricao)
)ENGINE=innoDB AUTO_INCREMENT = 1;
