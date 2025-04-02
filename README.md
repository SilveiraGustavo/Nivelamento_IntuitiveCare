# Processo seletivo para vaga de estágio IntuitiveCare

## Teste de Nivelamento 
Este repositório foi criado para a publicação dos conteúdos relacionados ao teste de nivelamento para a vaga de estágio em Engenharia de Software na empresa IntuitiveCare.

Nesta etapa, os candidatos devem implementar soluções para as tarefas propostas pela empresa. A IntuitiveCare disponibilizou uma lista com aproximadamente quatro desafios, para os quais devemos desenvolver soluções. Assim, este repositório armazenará as implementações, juntamente com instruções para a execução dos projetos e detalhes sobre a implementação.

## Projetos de Modo Geral 
Durante a análise do teste, observou-se que era possível escolher uma linguagem de programação entre as opções disponibilizadas pela empresa. Para a implementação das soluções, foi utilizada a linguagem Python, disponível para download no seguinte [link](https://www.python.org/downloads/).

Para o desenvolvimento de cada tarefa, foi criado um ambiente virtual utilizando o `venv`, com o objetivo de gerenciar de forma isolada as bibliotecas e dependências necessárias durante o processo de desenvolvimento. Esse procedimento garante que as versões das bibliotecas sejam controladas e compatíveis com o projeto, evitando conflitos com outras dependências ou projetos no sistema. Além disso, o uso de ambientes virtuais facilita a reprodução do ambiente de desenvolvimento em outras máquinas, garantindo maior flexibilidade e consistência.

Nas seções a seguir, fornecerei mais detalhes sobre as bibliotecas utilizadas em cada uma das tarefas.


##  Teste 1 Web Scraping - Detalhes da Implementação  
Este projeto realiza a extração e o download de anexos em PDF a partir de um site do governo, compactando os arquivos baixados em um `.zip`.  

### Funcionamento  
1. **Coleta de Links**: O código acessa a página-alvo e busca links de arquivos PDF que contenham "Anexo I" ou "Anexo II" no nome.  
2. **Download dos Arquivos**: Os arquivos encontrados são baixados e armazenados na pasta `anexos/`. Caso um arquivo com o mesmo nome já exista, um sufixo numérico é adicionado para evitar sobrescrita.  
3. **Compactação**: Após o download, todos os arquivos são agrupados em um único `.zip` chamado `anexos.zip`.  

### Estrutura do Código  
- `CriarDiretorio()`: Cria a pasta para armazenar os anexos.  
- `BaixarArquivo(url, caminho)`: Faz o download de um arquivo a partir de uma URL.  
- `ObterAnexos()`: Extrai os links dos PDFs da página especificada.  
- `NomeUnico(nome)`: Garante que o nome do arquivo seja único dentro da pasta.  
- `BaixarAnexos(anexos)`: Percorre a lista de anexos e baixa os arquivos.  
- `Compactar(arquivos)`: Gera o arquivo `.zip` com os PDFs baixados.  
- `Main()`: Função principal que orquestra todo o processo.  

### Execução  
#### Configuração do Ambiente Virtual  

Antes de executar o script, é recomendado configurar um ambiente virtual para gerenciar as dependências do projeto.  

1. **Criar o ambiente virtual**:
   
   ```sh
   python -m venv venv

2. **Ativação do ambiente virtual no Windows**:
     ```
     venv\Scripts\activate

3. **Instalar as dependências**:
   ```
   pip install requests beautifulsoup4
   
#### Rodando o script
  Com o ambiente virtual ativado e as dependências instaladas, execute:
  ```
  python Scraping.py
  ```

## Teste 2 Transformações de Dados -  Detalhes da implementação

Este projeto extrai dados de um `.pdf` governamental, salva em um arquivo `.csv` e compacta em um `.zip`.  



### Funcionamento  

1. **Extração de Tabelas:** O código lê todas as tabelas do arquivo `.pdf` especificado e as armazena em um DataFrame.  
2. **Formatação dos Dados:** Adiciona uma linha em branco entre cada tabela extraída para melhor organização.  
3. **Substituição de Abreviações:** Converte os valores "OD" e "AMB" para suas descrições completas.  
4. **Salvamento em CSV:** O DataFrame formatado é salvo como um arquivo `.csv`.  
5. **Compactação:** O arquivo `.csv` gerado é compactado em um ZIP chamado `Teste_Gustavo.zip` e o `.csv` original é removido após a compactação.
   

### Estrutura do Código  

- **Extrair_Tabelas(pdf_path):** Lê todas as tabelas do `.pdf` e as retorna como um DataFrame consolidado, adicionando uma linha vazia entre as tabelas extraídas.  
- **Substituir_Abreviacoes(df):** Substitui as abreviações "OD" e "AMB" por suas descrições completas.  
- **Salvar_Csv(df, nome_arquivo):** Salva os dados extraídos em um arquivo CSV.  
- **Compactar_Arquivo(csv_path, zip_path):** Compacta o arquivo `.csv` gerado em um arquivo `.zip` e remove o `.csv` após a compactação.  
- **Main():** Função principal que executa todo o fluxo do programa: extração de tabelas, formatação, salvamento, e compactação.
  
### Execução
#### Configuração do Ambiente Virtual  

Antes de executar o script, é recomendado configurar um ambiente virtual para gerenciar as dependências do projeto.  

Neste repositório, o arquivo `Tarefa2.txt` lista todas as dependências utilizadas na Tarefa 2. Para instalar os pacotes, é necessário que o ambiente virtual já esteja criado e ativado. Após isso, execute o seguinte comando para instalar os pacotes:

```
   pip install -r Tarefa2.txt
```
#### Rodando o script
  Com o ambiente virtual ativado e as dependências instaladas, execute:
  ```
  python Tarefa2.py
  ```


