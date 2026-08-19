# Dashboard de Inscrições em Cursos

![Google Sheets](https://img.shields.io/badge/Google%20Sheets-Dados-34A853?style=flat&logo=google-sheets&logoColor=white)
![Looker Studio](https://img.shields.io/badge/Looker%20Studio-Dashboard-4285F4?style=flat&logo=looker&logoColor=white)
![Data Visualization](https://img.shields.io/badge/Data%20Visualization-Dashboard-8A2BE2?style=flat)
![Status](https://img.shields.io/badge/Status-Concluído-2EA44F?style=flat)

Dashboard desenvolvido no **Google Looker Studio** para acompanhamento de inscrições em cursos, situação dos participantes e desempenho por curso.
O projeto utiliza uma planilha como fonte de dados e apresenta indicadores, gráficos, filtros interativos e uma tabela detalhada para facilitar a análise das inscrições.

---

##  Sobre o projeto

O objetivo deste projeto é transformar os dados de inscrições em cursos em um painel visual e organizado, permitindo uma análise rápida da quantidade de participantes, situação das inscrições e distribuição por curso.
O dashboard apresenta:

- Total de inscritos;
- Total de participantes concluídos;
- Total de participantes pendentes;
- Taxa de conclusão;
- Quantidade de inscrições por curso;
- Distribuição entre participantes concluídos e pendentes;
- Tabela detalhada das inscrições;
- Filtros por curso;
- Filtros por status;
- Filtro por período de inscrição;
- Resumo executivo dos principais indicadores.

---

##  Dashboard

O relatório foi desenvolvido no **Google Looker Studio**, utilizando uma planilha do Google Sheets como fonte de dados.

### Indicadores principais

- **Total de Inscritos:** 48
- **Concluídos:** 31
- **Pendentes:** 17
- **Taxa de Conclusão:** 64,58%

### Visualizações

O dashboard conta com:

- **Gráfico de barras:** quantidade de inscrições por curso;
- **Gráfico de rosca:** distribuição entre inscrições concluídas e pendentes;
- **Tabela:** relação detalhada dos participantes, cursos, status e datas de inscrição;
- **Filtros interativos:** curso, status e período.

---

##  Campo calculado

Foi criado um campo calculado para representar a taxa de conclusão:

```text
Taxa de Conclusão = Concluídos / Total de Inscritos
```

No conjunto apresentado no dashboard:

```text
31 / 48 = 64,58%
```

---

##  Dados

A base utilizada contém informações relacionadas às inscrições nos cursos:

| Campo | Descrição |
|---|---|
| Aluno | Nome do participante |
| Curso | Curso realizado ou selecionado |
| Status | Situação da inscrição |
| Data de Inscrição | Data em que a inscrição foi registrada |

---

##  Arquivos do projeto

```text
Dashboard Looker/
│
├── dados_dashboard_looker.xlsx
├── dashboard_inscricoes_cursos.pdf
└── README.md
```

- `dados_dashboard_looker.xlsx` — base de dados utilizada no projeto.
- `dashboard_inscricoes_cursos.pdf` — versão exportada do relatório desenvolvido no Looker Studio.
- `README.md` — documentação do projeto.

---

##  Tecnologias utilizadas

- **Google Sheets** — armazenamento e organização dos dados;
- **Google Looker Studio** — criação do dashboard e visualizações;
- **Excel (.xlsx)** — arquivo da base de dados;
- **PDF** — versão exportada do relatório.

---

##  Objetivos desenvolvidos

- Conectar uma planilha como fonte de dados;
- Criar indicadores de acompanhamento;
- Desenvolver diferentes tipos de gráficos;
- Criar campo calculado;
- Adicionar filtros interativos;
- Organizar os elementos em um dashboard único;
- Criar um resumo executivo para apresentação dos resultados.

---

##  Resultado

O dashboard permite visualizar rapidamente o cenário das inscrições e identificar a distribuição dos participantes entre os cursos e seus respectivos status.

Entre os principais resultados apresentados:

- 48 inscrições registradas;
- 31 participantes concluíram os cursos;
- 17 participantes permanecem pendentes;
- 64,58% de taxa de conclusão;
- **Atendimento ao Cidadão** apresenta a maior quantidade de inscrições.

---

##  Link

Acesse o link:

```bash
https://datastudio.google.com/reporting/55229670-1e6d-4170-a126-2257e241c478
```

---

## Autor

Desenvolvido por **Eduardo Henrique Brilhante**

---

<p align="center">
  Desenvolvido com Google Sheets e Looker Studio.
</p>
