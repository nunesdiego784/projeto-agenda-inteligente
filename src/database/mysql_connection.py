import pymysql
from pymysql.connections import Connection

class MySQLConnection:
    def __init__(self, host='localhost', user='root', password='', database='agenda_inteligente', port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    def conectar(self) -> Connection:
        """Estabelece e retorna uma conexão com o banco de dados MySQL."""
        try:
            conexao = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
                cursorclass=pymysql.cursors.DictCursor # Retorna os resultados como dicionários Python
            )
            return conexao
        except pymysql.MySQLError as e:
            print(f"Erro ao conectar ao MySQL: {e}")
            raise e