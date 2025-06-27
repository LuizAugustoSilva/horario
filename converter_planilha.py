import os
import pandas as pd

def geraDicionario():
    # Caminho da pasta com os arquivos CSV
    pasta = os.path.join(os.path.dirname(__file__), 'HorariosPessoais')

    horarios_vagos_por_arquivo = {}
    index_horario = {}
    cont = 1

    # Percorre todos os arquivos CSV da pasta
    for nome_arquivo in os.listdir(pasta):
        if nome_arquivo.endswith('.csv'):
            caminho_arquivo = os.path.join(pasta, nome_arquivo)
            df = pd.read_csv(caminho_arquivo)

            horarios_vagos_por_arquivo[nome_arquivo] = {}

            for index, row in df.iterrows():
                for coluna in df.columns:
                    valor = row[coluna]
                    if pd.isna(valor) or valor == 0:
                        horarios_vagos_por_arquivo[nome_arquivo][f"{row[df.columns[0]]} - {coluna}"] = cont
                        index_horario[cont] = f"{row[df.columns[0]]} - {coluna}"
                        cont += 1
            

    # Exibe o dicionário final
    return horarios_vagos_por_arquivo, index_horario, cont