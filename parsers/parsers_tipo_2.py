import os
import re
import json
import fitz


def extrair_faturas(doc):

    transacoes_finais = []

    termo_inclusao = "Lançamentos: compras e saques"
    padrao_transacao = r"(\d{2}/\d{2})\n(.+?)\n([\d.,]+)"

    for page_number, page in enumerate(doc, start=1):
        texto_pagina = page.get_text()

        if "Compras parceladas - próximas faturas" in texto_pagina:
            texto_pagina = texto_pagina.split("Compras parceladas - próximas faturas")[0]

        print(f"Processando transações da Página {page_number}...")

        transacoes_encontradas = re.findall(padrao_transacao, texto_pagina)

        for data, estabelecimento, valor in transacoes_encontradas:
            transacoes_finais.append({
                "pagina": page_number,
                "data": data.strip(),
                "estabelecimento": estabelecimento.strip(),
                "pais": "BR",
                "valor": valor.strip()
            })

    doc.close()
    return transacoes_finais