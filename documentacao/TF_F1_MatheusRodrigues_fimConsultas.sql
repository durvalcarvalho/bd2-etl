-- 	-------- Trabalho Final - Tema F1 - ETL - ENEM ----------
--
-- SCRIPT DE CONSULTA (DML e DDL)
--
-- Data Criacao ...........: 25/10/2021
-- Autor(es) ..............: Durval Carvalho e Matheus Gabriel
-- Banco de Dados .........: MySQL 8
-- Base de Dados (nome) ...: TF_Apr_F_MatheusRodrigues
--
-- PROJETO => 01 Base de Dados
--         => 04 Tabelas
--
-- ---------------------------------------------------------

USE TF_Apr_F_MatheusRodrigues;

CREATE OR REPLACE VIEW CANDIDATOS_DF AS
SELECT CANDIDATO.inscricao, CANDIDATO.sexo, notaRedacao, notaMatematica, notaHumanas, notaLinguagem, notaCiencias 
    FROM CANDIDATO 
    INNER JOIN realiza 
    ON CANDIDATO.inscricao = realiza.inscricaoCandidato 
    WHERE CANDIDATO.codMunicipio = 146;
