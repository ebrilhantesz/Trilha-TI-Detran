import os
from dotenv import load_dotenv

# Carrega as variáveis presentes no arquivo .env
load_dotenv()

# Recupera a variável API_KEY
api_key = os.getenv("API_KEY")

# Verifica se a variável foi encontrada
if api_key:
    print("Variável API_KEY lida com sucesso!")
else:
    print("A variável API_KEY não foi encontrada.")