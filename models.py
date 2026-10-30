from dataclasses import dataclass

@dataclass
class Transaction:
    data: str
    estabelecimento: str
    descricao: str
    valor: float

    categoria: str | None = None
    confidence: float = 0.0

