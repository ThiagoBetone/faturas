from parsers.parser_tipo_1 import extrair_faturas as parcer_tipo_1
from parsers.parsers_tipo_2 import extrair_faturas as parcer_tipo_2
import dotenv
import os

dotenv.load_dotenv()

banco_x = os.getenv('banco_um')
banco_y = os.getenv('banco_dois')
banco_z = os.getenv('banco_tres')

def obter_parser(texto):

    if banco_x in texto or banco_y in texto:
        return parcer_tipo_1

    if banco_z in texto:
        return parcer_tipo_2

    raise Exception("Banco não suportado.")