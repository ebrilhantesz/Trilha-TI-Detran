import os
import requests

from bs4 import BeautifulSoup
from dotenv import load_dotenv

def carregar_configuracoes():
    load_dotenv()
    os.environ["HTTP_PROXY"] = os.getenv("HTTP_PROXY", "")
    os.environ["HTTPS_PROXY"] = os.getenv("HTTPS_PROXY", "")
    os.environ["NO_PROXY"] = os.getenv("NO_PROXY", "")

def acessar_pagina(url):
    headers = {"User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/151.0.0.0 Safari/537.36")}
    resposta = requests.get(url, headers=headers)
    resposta.raise_for_status()
    return resposta

def processar_html(conteudo):
    return BeautifulSoup(conteudo, "html.parser")

def encontrar_cabecalho(soup):
    cabecalho = soup.find("h1")
    if cabecalho:
        return cabecalho.get_text(strip=True)
    cabecalho = soup.find("h2")
    if cabecalho:
        return cabecalho.get_text(strip=True)
    return None

def encontrar_link(soup):
    link = soup.find("a", href=True)
    if link:
        return {"texto": link.get_text(strip=True),"href": link.get("href")}
    return None

def main():
    print("=====================================")
    print("RASPAGEM COM REQUESTS E BEAUTIFULSOUP")
    print("=====================================")

    carregar_configuracoes()
    url = "https://www.detran.pr.gov.br/"

    try:
        print("\nAcessando página...")
        resposta = acessar_pagina(url)

        print(f"Status da requisição: {resposta.status_code}")

        print("\nProcessando HTML...")
        soup = processar_html(resposta.text)

        print("HTML processado com BeautifulSoup.")

        print("\nBuscando cabeçalho...")
        cabecalho = encontrar_cabecalho(soup)

        if cabecalho:
            print(f"Cabeçalho encontrado: {cabecalho}")
        else:
            print("Nenhum cabeçalho encontrado.")

        print("\nBuscando link...")
        link = encontrar_link(soup)

        if link:
            print(f"Texto: {link['texto']}")
            print(f"Href: {link['href']}")
        else:
            print("Nenhum link encontrado.")

    except requests.RequestException as erro:
        print(f"\nErro na requisição: {erro}")

if __name__ == "__main__":
    main()