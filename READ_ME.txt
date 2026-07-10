
Automatização da extração de informações de faturas bancárias em PDF utilizando Python, fitz e Expressões Regulares (Regex).

O objetivo do projeto é transformar documentos financeiros não estruturados em dados organizados (JSON), facilitando análises, integrações e automações.

---

## Funcionalidades

- Extração automática das transações da fatura
- Suporte a múltiplos layouts de bancos
- Exportação dos dados para JSON
- Arquitetura preparada para inclusão de novos bancos

---

##  Fluxo da aplicação

```text
        Fatura em PDF
              │
              ▼
     Leitura com fitz
              │
              ▼
 Identificação do Banco
              │
              ▼
 Parser específico
              │
              ▼
 Extração utilizando Regex
              │
              ▼
 Tratamento dos dados
              │
              ▼
      JSON estruturado
```

---

## Tecnologias utilizadas

- Python
- PyMuPDF (fitz)
- Regex
- JSON

---

## Entrada

O parser recebe uma fatura em PDF.

Exemplo:

```text
Fatura_banco.pdf
```

---

##  Saída

```json
[
    {
        "pagina": 1,
        "data": "15/06",
        "estabelecimento": "SUPERMERCADO XYZ",
        "valor": "89,90"
    },
    {
        "pagina": 1,
        "data": "18/06",
        "estabelecimento": "POSTO ABC",
        "valor": "120,00"
    }
]
```

---

##  Como executar

Clone o projeto

```bash
git clone https://github.com/seuusuario/invoice_parser.git
```

Instale as dependências

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env`

Execute

```bash
python main.py
```

---

## Motivação

Este projeto foi desenvolvido para praticar técnicas de extração de dados de documentos PDF, utilizando Python e Regex para automatizar tarefas repetitivas de processamento de documentos financeiros.

Além disso, o projeto foi estruturado pensando em escalabilidade, permitindo a inclusão de novos layouts de faturas de forma simples.

---
