from pathlib import Path

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def abrir_navegador():
    navegador = webdriver.Chrome()
    navegador.maximize_window()
    return navegador

def abrir_pagina(navegador):
    caminho_html = Path(__file__).resolve().parent / "consulta_cpf.html"
    if not caminho_html.exists():
        raise FileNotFoundError(f"Arquivo HTML não encontrado: {caminho_html}")
    navegador.get(caminho_html.as_uri())

def consultar_cpf(navegador, cpf):
    campo_cpf = WebDriverWait(navegador, 10).until(EC.presence_of_element_located(("id", "cpf")))
    campo_cpf.send_keys(cpf)

    botao_consultar = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable(("id", "consultar")))
    botao_consultar.click()

def obter_resultado(navegador):
    resultado = WebDriverWait(navegador, 10).until(EC.presence_of_element_located(("id", "registro")))
    return resultado.text

def main():
    print("==========================")
    print("SISTEMA DE CONSULTA DE CPF")
    print("==========================")

    navegador = abrir_navegador()

    try:
        print("\nAbrindo sistema de consulta...")
        abrir_pagina(navegador)

        cpf = "11111111111"

        print(f"Consultando CPF: {cpf}")
        consultar_cpf(navegador, cpf)

        resultado = obter_resultado(navegador)

        print("\nResultado da consulta:")
        print("--------------------")
        print(resultado)
        print("--------------------")
    finally:
        navegador.quit()

if __name__ == "__main__":
    main()