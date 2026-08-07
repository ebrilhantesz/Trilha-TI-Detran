# Refatoração e Revisão de Código: Cálculo e Validação de Notas

Este repositório contém a atividade de revisão de código (*code review*) e refatoração de um script Python para coleta, cálculo de média e avaliação do status de aprovação de estudantes.

---

## 📁 Estrutura do Repositório

```text
.
├── codigo_original.py   # Versão inicial do script (sem funções, variáveis não descritivas)
├── codigo_revisado.py   # Versão refatorada (modularizada, com tratamento de erros)
└── README.md            # Documentação e comparação entre as versões
```

---

## 🔍 Problemas Identificados no Código Original (`codigo_original.py`)

1. **Nomes de Variáveis Inexpressivos:** Uso de letras isoladas (`n`, `l`, `i`, `x`, `s`, `j`, `m`), o que prejudica a legibilidade e manutenibilidade do código.
2. **Ausência de Modularização:** Toda a lógica está escrita no escopo global sem o uso de funções reutilizáveis.
3. **Falta de Tratamento de Exceções:** Inexistência de blocos `try/except`. Caso o usuário digite um valor não numérico, o programa é interrompido abruptamente por `ValueError`.
4. **Falta de Validação de Domínio:** O sistema aceita notas negativas ou acima de 10 sem restrição.
5. **Redundância Iterativa:** Uso de loops manuais para ler e somar valores em vez de utilizar funções nativas do Python como `range()` e `sum()`.

---

## ✨ Melhorias Aplicadas (`codigo_revisado.py`)

- **Nomenclatura Clara:** Variáveis e funções renomeadas com nomes autoexplicativos (`coletar_notas`, `quantidade_notas`, `avaliar_desempenho`).
- **Modularização em Funções:** Divisão do programa em funções com responsabilidades únicas (`coletar_notas`, `avaliar_desempenho`, `main`).
- **Tratamento de Erros e Validação:** Adicionado bloco `try/except` com loop de repetição `while True` para garantir que apenas valores válidos (inteiros positivos para quantidade, e números entre 0 e 10 para notas) sejam aceitos.
- **Uso de Recursos Nativos:** Simplificação do cálculo da soma e média com as funções `sum()` e `len()`.

---

## 📊 Comparação entre as Versões

> **Resumo da Análise:**
> A versão revisada substituiu variáveis genéricas por nomes descritivos, organizou o fluxo em funções específicas e adicionou tratamento robusto de exceções (`try/except`). Essas alterações tornaram o programa imune a entradas inválidas, eliminaram redundâncias com o uso de `sum()` e garantiram maior clareza, segurança e facilidade de manutenção.

---

## 🚀 Como Executar

Para executar a versão revisada e testar os tratamentos de erro, utilize o terminal:

```bash
python3 codigo_revisado.py
```
