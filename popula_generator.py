import dask.dataframe as dd
import pandas as pd
from os.path import exists



if not exists("static/cleaned_data/baseFinal.csv"):
    file_path = "./static/raw_data/DADOS/MICRODADOS_ENEM_2019.csv"
    df = dd.read_csv(file_path, encoding="latin-1", sep = ';')

    basena = df[['NU_NOTA_REDACAO', 'TP_STATUS_REDACAO','NU_NOTA_CN', 'NU_NOTA_CH',
                'NU_NOTA_LC', 'NU_NOTA_MT', 'IN_TREINEIRO','NU_INSCRICAO', 'TP_SEXO',
                'NU_IDADE', 'TP_COR_RACA', 'SG_UF_RESIDENCIA', 'NO_MUNICIPIO_RESIDENCIA',
                'CO_PROVA_CN', 'CO_PROVA_CH', 'CO_PROVA_LC', 'CO_PROVA_MT',]]

    base = basena.dropna()
    base = base.compute()
    base.to_csv('./static/cleaned_data/baseFinal.csv', index=False)
    print('-- Os dados da tabela `Base` foram tratados e salvos no arquivo baseFinal.csv')

else:
    base = pd.read_csv("./static/cleaned_data/baseFinal.csv")


municipio = base[['SG_UF_RESIDENCIA', 'NO_MUNICIPIO_RESIDENCIA' ]]
municipio = municipio.drop_duplicates()
municipio.to_csv('./static/cleaned_data/municipio.csv', index=False)
print(('-- Os dados da tabela `Municipios` foram tratados e '
       'salvos no arquivo municipio.csv'))

prova = base[['CO_PROVA_CN', 'CO_PROVA_CH', 'CO_PROVA_LC', 'CO_PROVA_MT']]
prova = prova.drop_duplicates()
prova.to_csv('./static/cleaned_data/prova.csv', index=False)
print('-- Os dados da tabela `Prova` foram tratados e salvos no arquivo prova.csv')


candidato = base[['NU_INSCRICAO', 'TP_SEXO', 'NU_IDADE', 'TP_COR_RACA',
                  'NO_MUNICIPIO_RESIDENCIA']]
candidato = candidato.drop_duplicates()
candidato.to_csv('./static/cleaned_data/candidato.csv', index=False)
print(('-- Os dados da tabela `Candidato` foram tratados '
       'e salvos no arquivo candidato.csv'))


realiza = base[['NU_NOTA_REDACAO', 'TP_STATUS_REDACAO','NU_NOTA_CN',
                'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'IN_TREINEIRO']]

realiza = realiza.drop_duplicates()
realiza.to_csv('./static/cleaned_data/realiza.csv', index=False)
print('-- Os dados da tabela `realiza` foram tratados e salvos no arquivo realiza.csv')
