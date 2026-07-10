import fitz
import dotenv
import os

from parser_detect import obter_parser

from utils import salvar_em_json

dotenv.load_dotenv()

root = os.getenv("caminho")

doc = fitz.open(root)

texto = ""

for pagina in doc:
    texto += pagina.get_text()

parser = obter_parser(texto)

dados = parser(doc)

nome_arquvio = root.split("/")[1].removesuffix(".pdf")

salvar_em_json(dados, f'dados_extraidos/{nome_arquvio}.json')
