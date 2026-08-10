import os
import shutil
from collections import Counter

# Pasta onde estão os arquivos
pasta_downloads = "downloads_teste"

# Arquivos de teste
arquivos_teste = [
    "documento.pdf",
    "planilha.xlsx",
    "anotacoes.txt",
    "imagem.jpg",
    "apresentacao.pptx",
    "arquivo.zip"
]

# Cria a pasta de teste caso ela não exista
os.makedirs(pasta_downloads, exist_ok=True)

# Cria os arquivos vazios
for arquivo in arquivos_teste:
    caminho = os.path.join(pasta_downloads, arquivo)
    if not os.path.exists(caminho):
        open(caminho, "w").close()

print("==================================")
print("ORGANIZADOR AUTOMÁTICO DE ARQUIVOS")
print("==================================")

# Lista todos os arquivos da pasta
arquivos = os.listdir(pasta_downloads)

# Contador para armazenar a quantidade de arquivos por extensão
quantidade_por_extensao = Counter()

# Percorre todos os arquivos encontrados
for arquivo in arquivos:

    caminho_arquivo = os.path.join(pasta_downloads, arquivo)

    # Garante que somente arquivos sejam processados
    if not os.path.isfile(caminho_arquivo):
        continue

    # Obtém a extensão do arquivo
    extensao = os.path.splitext(arquivo)[1].lower()

    # Remove o ponto da extensão
    extensao = extensao.replace(".", "")

    # Caso o arquivo não possua extensão
    if not extensao:
        extensao = "sem_extensao"

    # Cria a subpasta da extensão
    pasta_extensao = os.path.join(pasta_downloads, extensao)
    os.makedirs(pasta_extensao, exist_ok=True)

    # Define o destino do arquivo
    destino = os.path.join(pasta_extensao, arquivo)

    # Move o arquivo
    shutil.move(caminho_arquivo, destino)

    # Atualiza o contador
    quantidade_por_extensao[extensao] += 1

# Exibe o resultado
print("\nArquivos organizados:")
print("-" * 50)

for extensao, quantidade in sorted(quantidade_por_extensao.items()):
    print(f"{extensao}/: {quantidade} arquivo(s)")

print("======================")
print("Organização concluída!")
print("======================")