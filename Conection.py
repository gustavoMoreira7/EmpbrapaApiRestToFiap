import requests
from bs4 import BeautifulSoup
from datetime import datetime

class Conection:

    def __init__(self, link,parameters):
        self.link = link
        self.parameters = parameters

    def ExtractTableVitinicultura(self,intention):

        date = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

        link = self.link
        parameters = self.parameters
        response = requests.get(link, params=parameters)

        if response.status_code == 200:
            urlPage = response.url
            responseEntri = requests.get(urlPage)

            #Find Table of Data
            html_content = responseEntri.content
            soup = BeautifulSoup(html_content, "html.parser")
            tabela = soup.find("table", class_="tb_base tb_dados")

            # Verify if table exists
            if tabela:
                linhas = []
                
                # Extract headers
                cabecalho = tabela.find("thead")
                if cabecalho:
                    cabecalho_texto = [th.get_text(strip=True) for th in cabecalho.find_all("th")]
                    linhas.append("\t".join(cabecalho_texto))
                
                # Extract body
                corpo = tabela.find("tbody")
                for linha in corpo.find_all("tr"):
                    colunas = linha.find_all("td")
                    linha_texto = [coluna.get_text(strip=True) for coluna in colunas]
                    linhas.append("\t".join(linha_texto))

                # Extract foot
                rodape = tabela.find("tfoot")
                if rodape:
                    rodape_texto = [td.get_text(strip=True) for td in rodape.find_all("td")]
                    linhas.append("\t".join(rodape_texto))

                with open(f"{intention} {date}.csv", "w") as arquivo_txt:
                    for linha in linhas:
                        arquivo_txt.write(linha + "\n")
                print("Tabela salva com sucesso")



            else:
                print("Nenhuma tabela foi encontrada.")

        else:
            return "error"


