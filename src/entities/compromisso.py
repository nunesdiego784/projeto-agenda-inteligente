from datetime import datetime

class Compromisso:
    def __init__(
        self,
        id_compromisso: int,
        id_categoria: int,
        titulo: str,
        descricao: str,
        data_inicio: datetime,
        data_fim: datetime,
        prioridade: str = "Média",
        status: str = "Pendente"
    ):
        self.id_compromisso = id_compromisso
        self.id_categoria = id_categoria
        self.titulo = titulo
        self.descricao = descricao
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.prioridade = prioridade  # ex: Alta, Média, Baixa
        self.status = status          # ex: Pendente, Em Andamento, Concluído, Cancelado

    def to_dict(self) -> dict:
        return {
            "id_compromisso": self.id_compromisso,
            "id_categoria": self.id_categoria,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "data_inicio": self.data_inicio.isoformat() if isinstance(self.data_inicio, datetime) else self.data_inicio,
            "data_fim": self.data_fim.isoformat() if isinstance(self.data_fim, datetime) else self.data_fim,
            "prioridade": self.prioridade,
            "status": self.status
        }