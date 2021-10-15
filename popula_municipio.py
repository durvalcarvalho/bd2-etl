import pandas as pd

df = pd.read_csv('static/cleaned_data/municipio.csv')
inicialString = 'USE TrabalhoFinal;\n\nINSERT INTO MUNICIPIO (codMunicipio,nomeMunicipio ) VALUES\n'
tmpStr = ''
count = 0
totalRows = len(df.index)
popula = open('popula_municipio.sql', 'w')
popula.write(inicialString)
for index, row in df.iterrows():
    count +=1
    tmpStr = '\t(\'{}\', \'{}\'),\n'.format(str(row['SG_UF_RESIDENCIA']).replace('"', ''),
                                                       str(row['NO_MUNICIPIO_RESIDENCIA']))
    popula.write(tmpStr);

popula.close()