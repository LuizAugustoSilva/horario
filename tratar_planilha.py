import pandas as pd
import os

def tratar_arquivo(caminho_arquivo):
    # Ler todo o arquivo como texto
    df = pd.read_csv(caminho_arquivo, header=None, dtype=str)

    df = df.drop(df.columns[0], axis=1)
    df = df.drop(df.columns[6], axis=1)
    df = df.drop(df.columns[6], axis=1)
    df = df.drop(df.columns[6], axis=1)
    df = df.drop(df.columns[6], axis=1)
    df = df.drop(df.columns[6], axis=1)
    df = df.drop([0, 7, 13], axis=0)

    # Resetar índice para manter a linha que será cabeçalho como 0
    df = df.reset_index(drop=True)

    # Agora a linha 0 será o cabeçalho
    df.columns = df.iloc[0]

    # Remover essa linha 0 dos dados
    df = df.drop(0, axis=0).reset_index(drop=True)

    return df
def converteDadosBrutos():
    pasta = "HorariosPessoais"
    # Processar todos os arquivos da pasta
    for nome_arquivo in os.listdir(pasta):
        if nome_arquivo.startswith("Planilha de Horários Pessoais - ") and nome_arquivo.endswith(".csv"):
            caminho_arquivo = os.path.join(pasta, nome_arquivo)
            
            df_tratado = tratar_arquivo(caminho_arquivo)

            nome_pessoa = nome_arquivo.replace("Planilha de Horários Pessoais - ", "").replace(".csv", "").strip()
            novo_nome = f"{nome_pessoa}.csv"
            caminho_saida = os.path.join(pasta, novo_nome)

            df_tratado.to_csv(caminho_saida, index=False)
            print(f"Arquivo exportado: {novo_nome}")