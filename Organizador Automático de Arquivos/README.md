# Organizador Automático de Arquivos em Python

Um programa desenvolvido em **Python** para automatizar a organização de arquivos de uma pasta. O script identifica a extensão de cada arquivo, cria uma subpasta correspondente e move o arquivo para o local adequado.
O projeto utiliza recursos da biblioteca padrão do Python, como `os` e `shutil`, sem necessidade de instalar bibliotecas externas.

---

## Tabela de Conteúdo

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Funciona](#como-funciona)
- [Como Executar](#como-executar)
- [Exemplo de Execução](#exemplo-de-execução)
- [Autor](#autor)

---

## Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos de **manipulação de arquivos e diretórios em Python**.
O programa utiliza uma pasta de teste chamada `downloads_teste`, contendo arquivos de diferentes extensões. Ao ser executado, o script identifica automaticamente o tipo de cada arquivo, cria uma subpasta para cada extensão e move os arquivos para suas respectivas pastas.
Ao final, o programa apresenta a quantidade de arquivos organizados em cada categoria.

---

## Funcionalidades

- Criação automática da pasta `downloads_teste`.
- Criação de arquivos de teste com diferentes extensões.
- Listagem dos arquivos utilizando `os.listdir()`.
- Identificação automática da extensão dos arquivos.
- Criação de subpastas utilizando `os.makedirs()`.
- Movimentação dos arquivos utilizando `shutil.move()`.
- Separação automática por tipo de arquivo.
- Contagem de arquivos organizados por extensão.
- Exibição do resultado no terminal.
- Verificação para processar somente arquivos.

---

## Estrutura do Projeto

```text
Organizador Automático de Arquivos/
│
├── organizador.py
│
└── downloads_teste/
    │
    ├── pdf/
    │   └── documento.pdf
    │
    ├── xlsx/
    │   └── planilha.xlsx
    │
    ├── txt/
    │   └── anotacoes.txt
    │
    ├── jpg/
    │   └── imagem.jpg
    │
    ├── pptx/
    │   └── apresentacao.pptx
    │
    └── zip/
        └── arquivo.zip
```

---

## Como Funciona

### 1. Criação da pasta de teste

O programa cria automaticamente a pasta:

```text
downloads_teste/
```

Caso ela já exista, o programa continua normalmente.

### 2. Criação dos arquivos

Para facilitar os testes, o programa cria arquivos vazios com diferentes extensões:

```text
documento.pdf
planilha.xlsx
anotacoes.txt
imagem.jpg
apresentacao.pptx
arquivo.zip
```

### 3. Listagem dos arquivos

O programa utiliza:

```python
os.listdir()
```

para obter todos os itens existentes dentro da pasta `downloads_teste`.

### 4. Identificação da extensão

A extensão de cada arquivo é identificada utilizando:

```python
os.path.splitext()
```

Por exemplo:

```text
documento.pdf → pdf
planilha.xlsx → xlsx
imagem.jpg → jpg
```

### 5. Criação das subpastas

Para cada extensão encontrada, o programa cria uma pasta correspondente utilizando:

```python
os.makedirs()
```

Caso a pasta já exista, ela não é recriada.

### 6. Movimentação dos arquivos

Depois de identificar a extensão e criar a pasta correspondente, o arquivo é movido utilizando:

```python
shutil.move()
```

Assim:

```text
documento.pdf
```

passa a ficar em:

```text
downloads_teste/pdf/documento.pdf
```

### 7. Contagem dos arquivos

O programa mantém um contador para registrar quantos arquivos foram organizados em cada subpasta.
Ao final, o resultado é apresentado no terminal.

---

## Como Executar

### Pré-requisitos

- Python 3 instalado na máquina.

Não é necessário instalar nenhuma biblioteca externa.

### Clone o repositório

```bash
git clone https://github.com/ebrilhantesz/Trilha-TI-Detran.git
```

### Acesse a pasta

```bash
cd "Organizador Automático de Arquivos"
```

### Execute o programa

```bash
python organizador.py
```

ou:

```bash
python3 organizador.py
```

---

## Exemplo de Execução

```text
==================================================
       ORGANIZADOR AUTOMÁTICO DE ARQUIVOS
==================================================

Arquivos organizados:
--------------------------------------------------
jpg/: 1 arquivo(s)
pdf/: 1 arquivo(s)
pptx/: 1 arquivo(s)
txt/: 1 arquivo(s)
xlsx/: 1 arquivo(s)
zip/: 1 arquivo(s)
--------------------------------------------------
Organização concluída!
```

Após a execução, a pasta `downloads_teste` estará organizada automaticamente:

```text
downloads_teste/
│
├── jpg/
│   └── imagem.jpg
│
├── pdf/
│   └── documento.pdf
│
├── pptx/
│   └── apresentacao.pptx
│
├── txt/
│   └── anotacoes.txt
│
├── xlsx/
│   └── planilha.xlsx
│
└── zip/
    └── arquivo.zip
```

---

## Autor

Desenvolvido por **Eduardo Henrique Brilhante**