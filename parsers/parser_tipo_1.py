import os
import re
import json
import fitz


def extrair_faturas(doc):

    transacoes_finais = []

    termo_inclusao = "Pagamentos/Créditos"
    #1. Data (\d{2}/\d{2}) | 2. Descrição (.+?) | 3. País ([A-Z]{2}) | 4. Valor ([\d.,-]+)
    padrao_transacao = r"(\d{2}/\d{2})\s*\n\s*(.+?)\s*\n\s*([A-Z]{2})\s*\n\s*R\$\s*([\d.,-]+)"

    for page_number, page in enumerate(doc, start=1):
        texto_pagina = page.get_text()

        # if termo_inclusao not in texto_pagina:
        #     print(f"Página {page_number} ignorada (Não contém lançamentos).")
        #     continue

        print(f"Processando transações da Página {page_number}...")

        # Executa a busca baseada no padrão do tipo escolhido
        transacoes_encontradas = re.findall(padrao_transacao, texto_pagina)
        print(page_number)
        for data, descricao, pais, valor in transacoes_encontradas:
            transacoes_finais.append({
                "pagina": page_number,
                "data": data.strip(),
                "estabelecimento": descricao.strip(),
                "pais": pais.strip(),
                "valor": valor.strip()
            })

    doc.close()
    return transacoes_finais

