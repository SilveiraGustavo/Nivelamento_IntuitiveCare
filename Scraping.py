import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

DIR = 'anexos'
ZIP = 'anexos.zip'
URL_BASE = 'https://www.gov.br'
URL_PAGINA = URL_BASE + '/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

def CriarDiretorio():
    os.makedirs(DIR, exist_ok=True)

def BaixarArquivo(url, caminho):
    r = requests.get(url)
    r.raise_for_status()
    with open(caminho, 'wb') as f:
        f.write(r.content)

def ObterAnexos():
    r = requests.get(URL_PAGINA)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, 'html.parser')
    anexos = []
    
    for link in soup.find_all('a', href=True):
        texto = link.text.strip()
        url = link['href']
        if ('Anexo I' in texto or 'Anexo II' in texto) and url.lower().endswith('.pdf'):
            if not url.startswith('http'):
                url = URL_BASE + url
            anexos.append((texto, url))
    return anexos

def NomeUnico(nome):
    base, ext = os.path.splitext(nome)
    i = 1
    novo = nome
    while os.path.exists(os.path.join(DIR, novo)):
        novo = f"{base}_{i}{ext}"
        i += 1
    return novo

def BaixarAnexos(anexos):
    arquivos = []
    for nome, url in anexos:
        nome_pdf = NomeUnico(f"{nome.replace(' ', '_')}.pdf")
        caminho = os.path.join(DIR, nome_pdf)
        try:
            BaixarArquivo(url, caminho)
            arquivos.append(caminho)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao baixar {nome}: {e}")
    return arquivos

def Compactar(arquivos):
    if not arquivos:
        print("Nenhum arquivo baixado.")
        return
    with ZipFile(ZIP, 'w') as zipf:
        for arquivo in arquivos:
            zipf.write(arquivo, os.path.basename(arquivo))

def Main():
    CriarDiretorio()
    anexos = ObterAnexos()
    if not anexos:
        print("Nenhum anexo encontrado.")
        return
    arquivos = BaixarAnexos(anexos)
    Compactar(arquivos)
    print(f"Anexos compactados em {ZIP}")

if __name__ == "__main__":
    Main()
