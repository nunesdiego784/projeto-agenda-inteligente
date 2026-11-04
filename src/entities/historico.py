from datetime import datetime

class Historico:
    def __init__(
        self,
        id_historico: int,
        id_compromisso: int,
        status_anterior: str,
        status_novo: str,
        data_alteracao: datetime = None,
        tipo_alteracao: str = "Atualização de Status"
    ):
        self.id_historico = id_historico
        self.id_compromisso = id_compromisso
        self.status_anterior = status_anterior
        self.status_novo = status_novo
        self.data_alteracao = data_alteracao or datetime.now()
        self.tipo_alteracao = tipo_alteracao

    def to_dict(self) -> dict:
        return {
            "id_historico": self.id_historico,
            "id_compromisso": self.id_compromisso,
            "status_anterior": self.status_anterior,
            "status_novo": self.status_novo,
            "data_alteracao": self.data_alteracao.isoformat() if isinstance(self.data_alteracao, datetime) else self.data_alteracao,
            "tipo_alteracao": self.tipo_alteracao
        }