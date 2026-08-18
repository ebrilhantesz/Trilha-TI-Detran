import os
import shutil
import logging
from collections import Counter

# Config do LOG
logging.basicConfig(
    filename="organizacao.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Config da Pasta
pasta_downloads = "downloads_teste"
arquivos_teste = [
    "documento.pdf",
    "planilha.xlsx",
    "anotacoes.txt",
    "imagem.jpg",
    "apresentacao.pptx",
    "arquivo.zip"]

# Preparação dos arquivos
os.makedirs(pasta_downloads, exist_ok=True)

for arquivo in arquivos_teste:
    caminho = os.path.join(pasta_downloads, arquivo)
    if not os.path.exists(caminho):
        open(caminho, "w").close()

# Inicio do Programa
print("==================================")
print("ORGANIZADOR AUTOMÁTICO DE ARQUIVOS")
print("==================================")

logging.info("Iniciando a organização dos arquivos")

# Organização dos arquivos
arquivos = os.listdir(pasta_downloads)
quantidade_por_extensao = Counter()

for arquivo in arquivos:
    caminho_arquivo = os.path.join(pasta_downloads, arquivo)

    if not os.path.isfile(caminho_arquivo):
        continue
    extensao = os.path.splitext(arquivo)[1].lower()
    extensao = extensao.replace(".", "")
    if not extensao:
        extensao = "sem_extensao"
    pasta_extensao = os.path.join(pasta_downloads, extensao)
    os.makedirs(pasta_extensao, exist_ok=True)
    destino = os.path.join(pasta_extensao, arquivo)

    try:
        shutil.move(caminho_arquivo, destino)
        quantidade_por_extensao[extensao] += 1
        logging.info("Arquivo movido com sucesso: %s -> %s",arquivo,destino)
    except Exception as erro:
        logging.error("Falha ao mover o arquivo: %s | Erro: %s",arquivo,erro)

# Resultado no terminal
print("\nArquivos organizados:")
print("---------------------")

for extensao, quantidade in sorted(quantidade_por_extensao.items()):
    print(f"{extensao}/: {quantidade} arquivo(s)")

print("======================")
print("Organização concluída!")
print("======================")

logging.info("Organização dos arquivos finalizada")

# Exibição do LOG
print("\nDiário da organização:")
print("======================")

try:
    with open("organizacao.log", "r", encoding="utf-8") as arquivo_log:
        conteudo_log = arquivo_log.read()
    print(conteudo_log)
except Exception as erro:
    print(f"Não foi possível abrir o arquivo de log: {erro}")