class Categoria:
    def __init__(self, id_categoria: int, nome_categoria: str, descricao: str = ""):
        self.id_categoria = id_categoria
        self.nome_categoria = nome_categoria
        self.descricao = descricao

    def to_dict(self) -> dict:
        return {
            "id_categoria": self.id_categoria,
            "nome_categoria": self.nome_categoria,
            "descricao": self.descricao
        }