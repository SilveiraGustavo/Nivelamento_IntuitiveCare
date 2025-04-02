import pandas as pd
import zipfile
import os
from tabula import read_pdf

def Extrair_Tabelas(pdf_path):
    tabelas = read_pdf(pdf_path, pages="all", multiple_tables=True)
    if tabelas:
        print(f"Número de tabelas extraídas: {len(tabelas)}")
        tabelas_com_espaco = []
        for tabela in tabelas:
            tabelas_com_espaco.append(tabela)
            tabelas_com_espaco.append(pd.DataFrame([[''] * len(tabela.columns)], columns=tabela.columns))  # Adiciona linha vazia
        return pd.concat(tabelas_com_espaco, ignore_index=True)
    return None

def Substituir_Abreviacoes(df):
    legenda = {"OD": "Procedimentos Odontológicos", "AMB": "Procedimentos Ambulatoriais"}
    df.replace({"OD": legenda["OD"], "AMB": legenda["AMB"]}, inplace=True)
    return df

def Salvar_Csv(df, nome_arquivo):
    df.to_csv(nome_arquivo, index=False, encoding='utf-8')

def Compactar_Arquivo(csv_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_path, os.path.basename(csv_path))
    os.remove(csv_path)  # Remove o CSV após a compactação

# Definições
teste_nome = "Teste_Gustavo.zip"
pdf_entrada = "Anexo_I.pdf"
csv_saida = "tabela_procedimentos.csv"

# Execução
try:
    df = Extrair_Tabelas(pdf_entrada)
    if df is not None:
        df = Substituir_Abreviacoes(df)
        Salvar_Csv(df, csv_saida)
        Compactar_Arquivo(csv_saida, teste_nome)
        print(f"Processo concluído. Arquivo compactado: {teste_nome}")
    else:
        print("Nenhuma tabela encontrada no PDF.")
except Exception as e:
    print(f"Erro: {e}")
