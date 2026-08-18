import logging

# --- Configuração do diário (feita uma vez, no começo do programa) ---
logging.basicConfig(
    filename="vendas.log",                              # nome do arquivo do diário
    level=logging.INFO,                                 # registra do nível INFO pra cima (INFO e ERROR)
    format="%(asctime)s - %(levelname)s - %(message)s"  # cada linha fica: hora - nível - mensagem
)

# Lista de vendas que o robô vai processar. O "abc" está errado de propósito.
vendas = ["150", "300", "abc", "220"]
total = 0

logging.info("Iniciando o processamento das vendas")            # aviso normal -> info

for venda in vendas:
    try:
        valor = int(venda)                                      # tenta transformar em número
        total = total + valor
        logging.info("Venda processada: R$ %s", venda)          # deu certo -> info
    except ValueError:
        logging.error("Valor inválido, não foi possível processar: %s", venda)  # deu erro -> error

logging.info("Processamento finalizado. Total vendido: R$ %s", total)  # aviso normal -> info
print("Terminou. Total vendido: R$", total)
