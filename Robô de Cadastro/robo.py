import logging
import os
import shutil
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuração
PASTA_PROJETO = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_ALUNOS = os.path.join(PASTA_PROJETO, "alunos_projeto_final.xlsx")
ARQUIVO_HTML = os.path.join(PASTA_PROJETO, "index.html")
ARQUIVO_PENDENCIAS = os.path.join(PASTA_PROJETO, "relatorio_pendencias.xlsx")
ARQUIVO_SUCESSO = os.path.join(PASTA_PROJETO, "relatorio_sucesso_historico.xlsx")
ARQUIVO_LOG = os.path.join(PASTA_PROJETO, "robo_cadastro.log")
PASTA_PROCESSADOS = os.path.join(PASTA_PROJETO, "processados")

logging.basicConfig(
    filename=ARQUIVO_LOG,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)

# Logging
logging.info("Iniciando o robô de cadastro.")
df = pd.read_excel(ARQUIVO_ALUNOS)
logging.info("Planilha carregada com %d aluno(s).", len(df))

# Selenium
opcoes = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=opcoes)
wait = WebDriverWait(driver, 10)
url_local = "file:///" + ARQUIVO_HTML.replace("\\", "/")
driver.get(url_local)
logging.info("Página local aberta: %s", url_local)

# Lista dos alunos que não foram cadastrados
nao_cadastrados = []

for _, aluno in df.iterrows():

    nome = str(aluno["Nome"]).strip()
    cpf = str(aluno["CPF"]).strip()
    whatsapp_valor = aluno["WhatsApp"]

    if pd.isna(whatsapp_valor) or str(whatsapp_valor).strip() == "":
        status = "WhatsApp ausente"

        logging.warning("Aluno não cadastrado: %s | CPF: %s | Motivo: %s",nome,cpf,status,)

        nao_cadastrados.append({"Nome": nome, "CPF": cpf, "Status": status,})
        continue

    whatsapp = str(whatsapp_valor).strip()

    # Cadastro via Selenium
    try:
        campo_nome = wait.until(EC.presence_of_element_located((By.ID, "nome")))
        campo_whatsapp = wait.until(EC.presence_of_element_located((By.ID, "whatsapp")))
        botao_cadastrar = wait.until(EC.element_to_be_clickable((By.ID, "cadastrar")))

        campo_nome.clear()
        campo_nome.send_keys(nome)
        campo_whatsapp.clear()
        campo_whatsapp.send_keys(whatsapp)

        botao_cadastrar.click()

        logging.info("Aluno cadastrado com sucesso: %s | WhatsApp: %s",nome,whatsapp,)

    except Exception as erro:
        status = f"Falha no cadastro: {erro}"

        logging.error(
            "Falha ao cadastrar o aluno: %s | CPF: %s | Erro: %s",nome,cpf,erro,)

        nao_cadastrados.append({"Nome": nome,"CPF": cpf,"Status": status,})

# BeautifulSoup
html_atualizado = driver.page_source
soup = BeautifulSoup(html_atualizado, "html.parser")
corpo_tabela = soup.find("tbody", id="corpo_tabela")
sucesso = []

if corpo_tabela:
    linhas = corpo_tabela.find_all("tr")
    for linha in linhas:
        colunas = linha.find_all("td")
        if len(colunas) >= 2:
            nome = colunas[0].get_text(strip=True)
            whatsapp = colunas[1].get_text(strip=True)
            sucesso.append({"Nome": nome,"WhatsApp": whatsapp,})

    logging.info("Histórico capturado com sucesso: %d registro(s).",len(sucesso),)

else:
    logging.error("Tabela de histórico não encontrada.")

driver.quit()
logging.info("Navegador encerrado.")

# Exportar relatórios
df_pendencias = pd.DataFrame(nao_cadastrados,columns=["Nome", "CPF", "Status"],)
df_sucesso = pd.DataFrame(sucesso,columns=["Nome", "WhatsApp"],)

df_pendencias.to_excel(ARQUIVO_PENDENCIAS, index=False)
df_sucesso.to_excel(ARQUIVO_SUCESSO, index=False)

logging.info("Relatório de pendências salvo em: %s",ARQUIVO_PENDENCIAS,)
logging.info("Relatório de sucesso salvo em: %s",ARQUIVO_SUCESSO,)

# Cópia dos relatórios para pasta processados
os.makedirs(PASTA_PROCESSADOS, exist_ok=True)

relatorios = [ARQUIVO_PENDENCIAS,ARQUIVO_SUCESSO,]

for relatorio in relatorios:
    try:
        destino = os.path.join(PASTA_PROCESSADOS,os.path.basename(relatorio),)
        shutil.copy2(relatorio, destino)

        logging.info("Relatório copiado com sucesso: %s -> %s",relatorio,destino,)

    except Exception as erro:
        logging.error("Falha ao copiar o relatório: %s | Erro: %s",relatorio,erro,)


# Resumo
total_processados = len(df)
total_sucesso = len(sucesso)
total_pendencias = len(nao_cadastrados)

print("================")
print("ROBÔ DE CADASTRO")
print("================")
print(f"Total processados: {total_processados}")
print(f"Cadastros com sucesso: {total_sucesso}")
print(f"Pendências: {total_pendencias}")
print("================")
print(f"Relatório de sucesso: {ARQUIVO_SUCESSO}")
print(f"Relatório de pendências: {ARQUIVO_PENDENCIAS}")
print(f"Log: {ARQUIVO_LOG}")
print("================")

logging.info("Processamento finalizado. Total: %d | Sucesso: %d | Pendências: %d",
    total_processados,
    total_sucesso,
    total_pendencias,)