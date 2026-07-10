import json


def salvar_em_json(dados, nome_arquivo="dados_do_pdf.json"):
    print(f'\nSalvando dados extraídos. Total de transações coletadas: {len(dados)}')
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
    print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")
    