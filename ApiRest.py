from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import Conection as c
import uvicorn

app = FastAPI()

@app.get('/tabela_producao/{ano}')
async def ProductionExtract(ano: str):
    # Obtenha os parâmetros da URL
    ano = ano
    opcao = "opt_02"

    # Crie a conexão com os parâmetros fornecidos
    link = 'http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        "ano": ano,
        "opcao": opcao 
    }

    conection = c.Conection(link, params)
    
    # Extraia a tabela
    table = conection.ExtractTableVitinicultura("ProductionExtract")

    # Retorne os dados em formato JSON
    return JSONResponse(content=table)



@app.get('/tabela_processamento/{ano}/{filtro}')
async def ProcessingExtract(ano: str, filtro: str):

    # FILTROS
    # VINIFERAS = SUBOPT_01
    # AMERICANAS_E_HIBRIDAS = SUBOPT_02
    # UVAS_DE_MESA = SUBOPT_03
    # SEM_CLASSIFICAÇÃO = SUBOPT_04
    
    # Obtenha os parâmetros da URL
    ano = ano
    opcao = "opt_03"

    # Crie a conexão com os parâmetros fornecidos
    link = 'http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        "ano": ano,
        "opcao": opcao,
        "filtro": filtro
    }

    conection = c.Conection(link, params)
    
    # Extraia a tabela
    table = conection.ExtractTableVitinicultura("processamento")

    # Retorne os dados em formato JSON
    return JSONResponse(content=table)



@app.get('/tabela_comercializacao/{ano}')
async def MarketingExtract(ano: str):
    # Obtenha os parâmetros da URL
    ano = ano
    opcao = "opt_04"

    # Crie a conexão com os parâmetros fornecidos
    link = 'http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        "ano": ano,
        "opcao": opcao 
    }

    conection = c.Conection(link, params)
    
    # Extraia a tabela
    table = conection.ExtractTableVitinicultura("comercializacao")

    # Retorne os dados em formato JSON
    return JSONResponse(content=table)



@app.get('/tabela_importacao/{ano}/{filtro}')
async def ImportExtract(ano: str, filtro: str):

    # FILTROS
    # VINHOS_DE_MESA = SUBOPT_01
    # ESPUMANTES = SUBOPT_02
    # UVAS_FRESCAS = SUBOPT_03
    # UVAS_PASSAS = SUBOPT_04
    # SUCO_DE_UVA = SUBOPT_05
    
    # Obtenha os parâmetros da URL
    ano = ano
    opcao = "opt_05"

    # Crie a conexão com os parâmetros fornecidos
    link = 'http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        "ano": ano,
        "opcao": opcao,
        "filtro": filtro
    }

    conection = c.Conection(link, params)
    
    # Extraia a tabela
    table = conection.ExtractTableVitinicultura("importacao")

    # Retorne os dados em formato JSON
    return JSONResponse(content=table)



@app.get('/tabela_exportacao/{ano}/{filtro}')
async def ExportExtract(ano: str, filtro: str):

    # FILTROS
    # VINHOS_DE_MESA = SUBOPT_01
    # ESPUMANTES = SUBOPT_02
    # UVAS_FRESCAS = SUBOPT_03
    # SUCO_DE_UVA = SUBOPT_04
    
    # Obtenha os parâmetros da URL
    ano = ano
    opcao = "opt_06"

    # Crie a conexão com os parâmetros fornecidos
    link = 'http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        "ano": ano,
        "opcao": opcao,
        "filtro": filtro
    }

    conection = c.Conection(link, params)
    
    # Extraia a tabela
    table = conection.ExtractTableVitinicultura("exportacao")

    # Retorne os dados em formato JSON
    return JSONResponse(content=table)


if __name__ == '__main__':
    uvicorn.run(app)