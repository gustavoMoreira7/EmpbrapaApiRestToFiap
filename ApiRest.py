from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
import Conection as c
import uvicorn
import os
from azure.storage.blob import BlobServiceClient

app = FastAPI()

AZURE_CONNECTION_STRING = os.getenv('AZURE_CONNECTION_STRING')
AZURE_CONTAINER_NAME = "fiap"  # Nome do seu contêiner

@app.get("/")
async def read_root():
    return {"Hello": """
            
\n\n

Essa é a API responsavel pela extratificação de dados da empresa Embrapa\n\n
Não esqueça de verificar todos os EndPoints em nossa documentação...
            
\n\n

"""}

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204)  # Retorna um 204 No Content

@app.get('/tabela_producao/{ano}')
async def ProductionExtract(ano: str):
    # Obtenha os parâmetros da URL

    try:
        ano = ano
        opcao = "opt_02"

        # Crie a conexão com os parâmetros fornecidos
        link = 'http://vitibrasil.cnpuv.embrapa.br/index.php'
        params = {
            "ano": ano,
            "opcao": opcao 
        }

        conection = c.Conection(link, params)
        
        csv_content = conection.ExtractTableVitinicultura("ProductionExtract")

        if csv_content:
            return Response(content=csv_content, media_type='text/csv', headers={"Content-Disposition": "attachment; filename=production_data.csv"})
        else:
            return {"error": "Nenhuma tabela encontrada."}
    
    except:

        if int(ano) < 2019:
            return {"error": "O período especificado não pode ser encontrado no backup do azure."}

        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=AZURE_CONTAINER_NAME, blob=f"embrapa/producao/Producao_{ano}.csv")
        
        # Faz o download do blob para um buffer em memória
        download_stream = blob_client.download_blob()
        csv_content = download_stream.readall()

        # Retorna o conteúdo CSV como resposta
        return Response(content=csv_content, media_type='text/csv', headers={"Content-Disposition": f"attachment; filename=production_data_azure_backup_{ano}.csv", "X-Source": "Azure"})





@app.get('/tabela_processamento/{ano}/{filtro}')
async def ProcessingExtract(ano: str, filtro: str):

    # FILTROS
    # VINIFERAS = SUBOPT_01
    # AMERICANAS_E_HIBRIDAS = SUBOPT_02
    # UVAS_DE_MESA = SUBOPT_03
    # SEM_CLASSIFICAÇÃO = SUBOPT_04

    try:
        
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

        csv_content = conection.ExtractTableVitinicultura("processamento")

        if csv_content:
            return Response(content=csv_content, media_type='text/csv', headers={"Content-Disposition": "attachment; filename=production_data.csv"})
        else:
            return {"error": "Nenhuma tabela encontrada."}
        
    except:

        # VINIFERAS = SUBOPT_01
        # AMERICANAS_E_HIBRIDAS = SUBOPT_02
        # UVAS_DE_MESA = SUBOPT_03
        # SEM_CLASSIFICAÇÃO = SUBOPT_04

        if filtro == 'subopt_01':
            namearchive = 'Viniferas'

        elif filtro == 'subopt_02':
            namearchive = 'Americanas'

        elif filtro == 'subopt_03':
            namearchive = 'Mesa'

        elif filtro == 'subopt_04':
            namearchive = 'sem'

        else:
            return {"error": "A opcao especificada não pode ser encontrada no backup do azure."}
        
        if int(ano) < 2020:
            return {"error": "O período especificado não pode ser encontrado no backup do azure."}

        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=AZURE_CONTAINER_NAME, blob=f"embrapa/processamento/Processa{namearchive}_{ano}.csv")
        
        # Faz o download do blob para um buffer em memória
        download_stream = blob_client.download_blob()
        csv_content = download_stream.readall()

        # Retorna o conteúdo CSV como resposta
        return Response(content=csv_content, media_type='text/csv', headers={"Content-Disposition": f"attachment; filename=process_data_azure_backup_{ano}.csv", "X-Source": "Azure"})
    



@app.get('/tabela_comercializacao/{ano}')
async def MarketingExtract(ano: str):

    try:
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

        csv_content = conection.ExtractTableVitinicultura("comercializacao")

        if csv_content:
            return Response(content=csv_content, media_type='text/csv', headers={"Content-Disposition": "attachment; filename=production_data.csv"})
        else:
            return {"error": "Nenhuma tabela encontrada."}

    except:

        if int(ano) < 2020:
            return {"error": "O período especificado não pode ser encontrado no backup do azure."}

        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=AZURE_CONTAINER_NAME, blob=f"embrapa/comercio/Comercio_{ano}.csv")
        
        # Faz o download do blob para um buffer em memória
        download_stream = blob_client.download_blob()
        csv_content = download_stream.readall()

        # Retorna o conteúdo CSV como resposta
        return Response(content=csv_content, media_type='text/csv', headers={"Content-Disposition": f"attachment; filename=comercialization_data_azure_backup_{ano}.csv", "X-Source": "Azure"})


    



@app.get('/tabela_importacao/{ano}/{filtro}')
async def ImportExtract(ano: str, filtro: str):

    try:

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
        
        csv_content = conection.ExtractTableVitinicultura("importacao")

        if csv_content:
            return Response(content=csv_content, media_type='text/csv', headers={"Content-Disposition": "attachment; filename=production_data.csv"})
        else:
            return {"error": "Nenhuma tabela encontrada."}
        
    except:

        # VINHOS_DE_MESA = SUBOPT_01
        # ESPUMANTES = SUBOPT_02
        # UVAS_FRESCAS = SUBOPT_03
        # UVAS_PASSAS = SUBOPT_04
        # SUCO_DE_UVA = SUBOPT_05

        if filtro == 'subopt_01':
            namearchive = 'Vinhos'

        elif filtro == 'subopt_02':
            namearchive = 'Espumantes'

        elif filtro == 'subopt_03':
            namearchive = 'Frescas'

        elif filtro == 'subopt_04':
            namearchive = 'Passas'

        elif filtro == 'subopt_05':
            namearchive = 'Suco'

        else:
            return {"error": "A opcao especificada não pode ser encontrada no backup do azure."}
        
        if int(ano) < 2020:
            return {"error": "O período especificado não pode ser encontrado no backup do azure."}

        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=AZURE_CONTAINER_NAME, blob=f"embrapa/importacao/Imp{namearchive}_{ano}.csv")
        
        # Faz o download do blob para um buffer em memória
        download_stream = blob_client.download_blob()
        csv_content = download_stream.readall()

        # Retorna o conteúdo CSV como resposta
        return Response(content=csv_content, media_type='text/csv', headers={"Content-Disposition": f"attachment; filename=importation_data_azure_backup_{ano}.csv", "X-Source": "Azure"})
    






@app.get('/tabela_exportacao/{ano}/{filtro}')
async def ExportExtract(ano: str, filtro: str):

    try:

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
        
        csv_content = conection.ExtractTableVitinicultura("exportacao")

        if csv_content:
            return Response(content=csv_content, media_type='text/csv', headers={"Content-Disposition": "attachment; filename=production_data.csv"})
        else:
            return {"error": "Nenhuma tabela encontrada."}
    
    except:

        # VINHOS_DE_MESA = SUBOPT_01
        # ESPUMANTES = SUBOPT_02
        # UVAS_FRESCAS = SUBOPT_03
        # SUCO_DE_UVA = SUBOPT_04

        if filtro == 'subopt_01':
            namearchive = 'Vinho'

        elif filtro == 'subopt_02':
            namearchive = 'Espumantes'

        elif filtro == 'subopt_03':
            namearchive = 'Uva'

        elif filtro == 'subopt_04':
            namearchive = 'Suco'

        else:
            return {"error": "A opcao especificada não pode ser encontrada no backup do azure."}
        
        if int(ano) < 2020:
            return {"error": "O período especificado não pode ser encontrado no backup do azure."}

        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=AZURE_CONTAINER_NAME, blob=f"embrapa/exportacao/Exp{namearchive}_{ano}.csv")
        
        # Faz o download do blob para um buffer em memória
        download_stream = blob_client.download_blob()
        csv_content = download_stream.readall()

        # Retorna o conteúdo CSV como resposta
        return Response(content=csv_content, media_type='text/csv', headers={"Content-Disposition": f"attachment; filename=exportation_data_azure_backup_{ano}.csv", "X-Source": "Azure"})
    






if __name__ == "__main__":
    # Definindo a porta para o ambiente do Heroku
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)