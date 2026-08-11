import pandas as pd

funcionarios = {
    "Nome": ["Douglas Ribeiro", "Eduardo Brilhante", "Caio Santos"],
    "CPF": ["123.456.789-00", "987.654.321-00", "456.789.123-00"],
    "Status": ["Regular", "Pendente", "Regular"]
}

df = pd.DataFrame(funcionarios)

# Filtra apenas os funcionários com pendência
pendencias = df[df["Status"] == "Pendente"]

# Salva o relatório em Excel
pendencias.to_excel("relatorio_pendencias.xlsx", index=False)

print("=======================")
print("Relatório de Pendências")
print("=======================")

print("\nDataFrame completo:")
print(df)

print("\nFuncionários com pendências")
print(pendencias)

print("\nArquivo 'relatorio_pendencias.xlsx' criado com sucesso!")