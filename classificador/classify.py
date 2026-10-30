from keywords import CATEGORIAS
import json

def classify_keywords(description):

    text = description.upper()

    for category, words in CATEGORIAS.items():

        for word in words:

            if word in text:
                print(f'texto origianl: {text} - categoria retornada: {category}')
                return category

    return None

if __name__ == '__main__':
    with open('../dados_extraidos/fatura_itau_maio.json', 'r', encoding='utf8') as f:
        dados = json.load(f)

cont = 0
for dado in dados:
    texto = classify_keywords(dado['estabelecimento'])

    if texto != None:
        cont+=1
print(f'\n############## RESULTADOS DA CLASSIFICAÇÃO POR KEYWORDS ##############')
print(f'Total de dados a serem classificados: {len(dados)}\n Dados classificados: {cont}')
print(f'Porcentagem de acertos: {round(cont/len(dados)*100,2)}%')

