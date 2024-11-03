# Documentação da API de Extração de Dados de Viticultura

## Visão Geral
Esta API foi construída com o FastAPI para realizar a extração de tabelas de dados vitícolas de diferentes categorias, como produção, processamento, comercialização, importação e exportação, para um determinado ano e, em alguns casos, com filtros adicionais. A API utiliza uma classe `Conection` do módulo `Conection`, responsável por criar uma conexão e extrair tabelas específicas.

## Dependências
Para executar o código, as seguintes bibliotecas e módulos são necessários:
- **FastAPI**: Para criação de APIs.
- **uvicorn**: Para servir a aplicação FastAPI.
- **Conection**: Módulo personalizado que lida com a conexão e extração de dados (assume-se que `Conection` é uma classe neste módulo que inclui métodos específicos).
- **JSONResponse**: Para retornar respostas no formato JSON.

## Estrutura Geral
Cada endpoint recebe um ano e, em alguns casos, um filtro adicional. A API cria uma conexão com uma URL pré-definida e retorna dados extraídos no formato JSON.

---

## Endpoints

### 1. `/tabela_producao/{ano}`
- **Descrição**: Extrai dados de produção para um determinado ano.
- **Método**: `GET`
- **Parâmetros**:
  - `ano` (string): Ano para o qual os dados de produção são solicitados.
- **Processo**:
  - Define `opcao = "opt_02"`.
  - Constrói o link de conexão e parâmetros.
  - Utiliza o método `ExtractTableVitinicultura("ProductionExtract")` da classe `Conection` para extrair a tabela.
- **Retorno**: Dados JSON contendo a tabela de produção.

**Exemplo de Uso**:
  bash
  GET /tabela_producao/2023'

### 2. `/tabela_processamento/{ano}/{filtro}'
- Descrição: Extrai dados de processamento para um determinado ano com base em um filtro de tipo de uva.
-	Método: GET
-	Parâmetros:
--	ano (string): Ano para o qual os dados de processamento são solicitados.
--	filtro (string): Filtro para o tipo de uva. Opções disponíveis:
  -	SUBOPT_01: Viníferas
  -	SUBOPT_02: Americanas e Híbridas
  -	SUBOPT_03: Uvas de Mesa
  -	SUBOPT_04: Sem Classificação


-	Processo:
  -	Define opcao = "opt_03".
  -	Constrói o link de conexão e parâmetros, incluindo o filtro.
  -	Utiliza ExtractTableVitinicultura("processamento") para extrair a tabela.
  -	Retorno: Dados JSON contendo a tabela de processamento.

- Exemplo de Uso:
  bash
  GET /tabela_processamento/2023/SUBOPT_01

3. /tabela_comercializacao/{ano}
Descrição: Extrai dados de comercialização para um determinado ano.
-	Método: GET
-	Parâmetros:
  -	ano (string): Ano para o qual os dados de comercialização são solicitados.
    
-	Processo:
  -	Define opcao = "opt_04".
  -	Constrói o link de conexão e parâmetros.
  -	Utiliza ExtractTableVitinicultura("comercializacao") para extrair a tabela.
  -	Retorno: Dados JSON contendo a tabela de comercialização.
    
Exemplo de Uso:
  bash
  GET /tabela_comercializacao/2023
  
4. /tabela_importacao/{ano}/{filtro}
Descrição: Extrai dados de importação para um determinado ano com base em um filtro de tipo de produto.

-	Método: GET
-	Parâmetros:
  -	ano (string): Ano para o qual os dados de importação são solicitados.
  -	filtro (string): Filtro para o tipo de produto. Opções disponíveis:
    -	SUBOPT_01: Vinhos de Mesa
    -	SUBOPT_02: Espumantes
    -	SUBOPT_03: Uvas Frescas
    -	SUBOPT_04: Uvas Passas
    -	SUBOPT_05: Suco de Uva
      
-	Processo:
  -	Define opcao = "opt_05".
  -	Constrói o link de conexão e parâmetros, incluindo o filtro.
  -	Utiliza ExtractTableVitinicultura("importacao") para extrair a tabela.
  -	Retorno: Dados JSON contendo a tabela de importação.
  
Exemplo de Uso:
  bash
  GET /tabela_importacao/2023/SUBOPT_01

  
5. /tabela_exportacao/{ano}/{filtro}
Descrição: Extrai dados de exportação para um determinado ano com base em um filtro de tipo de produto.

-	Método: GET
-	Parâmetros:
  -	ano (string): Ano para o qual os dados de exportação são solicitados.
  -	filtro (string): Filtro para o tipo de produto. Opções disponíveis:
    -	SUBOPT_01: Vinhos de Mesa
    -	SUBOPT_02: Espumantes
    -	SUBOPT_03: Uvas Frescas
    -	SUBOPT_04: Suco de Uva
      
-	Processo:
  -	Define opcao = "opt_06".
  -	Constrói o link de conexão e parâmetros, incluindo o filtro.
  -	Utiliza ExtractTableVitinicultura("exportacao") para extrair a tabela.
  -	Retorno: Dados JSON contendo a tabela de exportação.]
    
Exemplo de Uso:
  bash
  GET /tabela_exportacao/2023/SUBOPT_02
