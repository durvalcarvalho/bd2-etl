import pandas as pd

def generate_prova_insert_sql():

    with open('static/cleaned_data/prova.csv') as input_file,\
         open('popula_prova.sql', 'w')         as output_file:

        cmd = (
            f"INSERT INTO PROVA \n"
             "    (idProva, corCiencias, corMatematica, corHumanas, corLinguagem)\n"
             "VALUES\n"
        )

        print(cmd, file=output_file)

        for i, raw_line in enumerate(input_file):
            if i == 0: continue # header
            line = raw_line.strip()

            data = line.split(',')



if __name__ == "__main__":
    generate_prova_insert_sql()