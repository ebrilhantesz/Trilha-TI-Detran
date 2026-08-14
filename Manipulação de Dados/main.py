import os
import gspread
import pandas as pd

from dotenv import load_dotenv

def carregar_configuracoes():

    load_dotenv()

    os.environ["HTTP_PROXY"] = os.getenv("HTTP_PROXY", "")
    os.environ["HTTPS_PROXY"] = os.getenv("HTTPS_PROXY", "")
    os.environ["NO_PROXY"] = os.getenv("NO_PROXY", "")

    credencial_google = os.getenv("GOOGLE_CREDENTIALS_PATH")

    if not credencial_google:
        raise ValueError("GOOGLE_CREDENTIALS_PATH não foi encontrado no .env.")
    if not os.path.isfile(credencial_google):
        raise FileNotFoundError(f"Credencial Google não encontrada: {credencial_google}")
    return credencial_google

def conectar_google_sheets(caminho_credencial):

    return gspread.service_account(filename=caminho_credencial)

def ler_planilha(gp, nome_planilha):

    planilha = gp.open(nome_planilha)
    aba = planilha.sheet1
    dados_puros = aba.get_all_values()

    if not dados_puros:raise ValueError("A planilha está vazia.")
    df = pd.DataFrame(dados_puros[1:],columns=dados_puros[0])
    return planilha, df

def filtrar_pendentes(df):

    if "Status" not in df.columns:
        raise ValueError("A coluna 'Status' não foi encontrada na planilha.")
    return df[df["Status"] == "Pendente"]

def escrever_pendentes(planilha, pendentes):

    nome_aba = "Pendentes"
    try:
        aba_pendentes = planilha.worksheet(nome_aba)
        print(f"A aba '{nome_aba}' já existe.")
    except gspread.WorksheetNotFound:
        aba_pendentes = planilha.add_worksheet(title=nome_aba,rows=100,cols=10)
        print(f"A aba '{nome_aba}' foi criada.")

    dados_pendentes = [pendentes.columns.tolist()] + pendentes.astype(str).values.tolist()
    aba_pendentes.clear()
    aba_pendentes.update(range_name="A1",values=dados_pendentes)

    print(f"Dados gravados na aba '{nome_aba}'.")

def main():

    print("==================================")
    print("LEITURA DE ALUNOS DO GOOGLE SHEETS")
    print("==================================")

    credencial_google = carregar_configuracoes()
    print("\nCredencial Google encontrada.")

    gp = conectar_google_sheets(credencial_google)
    print("Conexão com Google Sheets realizada.")

    planilha, df = ler_planilha(gp,"teste_alunos")
    print("\nDados da planilha:")
    print(df)

    pendentes = filtrar_pendentes(df)

    print("\n" + "==========================")
    print("ALUNOS COM STATUS PENDENTE")
    print("==========================")

    print(pendentes)
    print(f"\nQuantidade de alunos pendentes: {len(pendentes)}")

    escrever_pendentes(planilha,pendentes)

if __name__ == "__main__":
    main()