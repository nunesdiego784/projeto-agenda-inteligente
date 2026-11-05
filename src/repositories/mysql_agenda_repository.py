from typing import List, Optional
from datetime import datetime
from src.database.mysql_connection import MySQLConnection
from src.entities.categoria import Categoria
from src.entities.compromisso import Compromisso
from src.entities.historico import Historico

class MySQLAgendaRepository:
    def __init__(self, db_connection: MySQLConnection):
        self.db_connection = db_connection

    # --- Operações de Categoria ---
    def salvar_categoria(self, nome_categoria: str, descricao: str) -> Categoria:
        conexao = self.db_connection.conectar()
        try:
            with conexao.cursor() as cursor:
                sql = "INSERT INTO categoria (nome_categoria, descricao) VALUES (%s, %s)"
                cursor.execute(sql, (nome_categoria, descricao))
                conexao.commit()
                id_gerado = cursor.lastrowid
                return Categoria(
                    id_categoria=id_gerado,
                    nome_categoria=nome_categoria,
                    descricao=descricao
                )
        finally:
            conexao.close()

    def listar_categorias(self) -> List[Categoria]:
        conexao = self.db_connection.conectar()
        try:
            with conexao.cursor() as cursor:
                sql = "SELECT id_categoria, nome_categoria, descricao FROM categoria"
                cursor.execute(sql)
                resultados = cursor.fetchall()
                return [
                    Categoria(
                        id_categoria=row['id_categoria'],
                        nome_categoria=row['nome_categoria'],
                        descricao=row['descricao']
                    ) for row in resultados
                ]
        finally:
            conexao.close()

    def buscar_categoria_por_id(self, id_categoria: int) -> Optional[Categoria]:
        conexao = self.db_connection.conectar()
        try:
            with conexao.cursor() as cursor:
                sql = "SELECT id_categoria, nome_categoria, descricao FROM categoria WHERE id_categoria = %s"
                cursor.execute(sql, (id_categoria,))
                row = cursor.fetchone()
                if row:
                    return Categoria(
                        id_categoria=row['id_categoria'],
                        nome_categoria=row['nome_categoria'],
                        descricao=row['descricao']
                    )
                return None
        finally:
            conexao.close()

    # --- Operações de Compromisso ---
    def salvar_compromisso(
        self,
        id_categoria: int,
        titulo: str,
        descricao: str,
        data_inicio,
        data_fim,
        prioridade: str = "Média",
        status: str = "Pendente"
    ) -> Compromisso:
        conexao = self.db_connection.conectar()
        try:
            with conexao.cursor() as cursor:
                sql = """
                    INSERT INTO compromisso (id_categoria, titulo, descricao, data_inicio, data_fim, prioridade, status)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (id_categoria, titulo, descricao, data_inicio, data_fim, prioridade, status))
                conexao.commit()
                id_gerado = cursor.lastrowid
                return Compromisso(
                    id_compromisso=id_gerado,
                    id_categoria=id_categoria,
                    titulo=titulo,
                    descricao=descricao,
                    data_inicio=data_inicio,
                    data_fim=data_fim,
                    prioridade=prioridade,
                    status=status
                )
        finally:
            conexao.close()

    def listar_compromissos(self) -> List[Compromisso]:
        conexao = self.db_connection.conectar()
        try:
            with conexao.cursor() as cursor:
                sql = "SELECT id_compromisso, id_categoria, titulo, descricao, data_inicio, data_fim, prioridade, status FROM compromisso"
                cursor.execute(sql)
                resultados = cursor.fetchall()
                return [
                    Compromisso(
                        id_compromisso=row['id_compromisso'],
                        id_categoria=row['id_categoria'],
                        titulo=row['titulo'],
                        descricao=row['descricao'],
                        data_inicio=row['data_inicio'],
                        data_fim=row['data_fim'],
                        prioridade=row['prioridade'],
                        status=row['status']
                    ) for row in resultados
                ]
        finally:
            conexao.close()

    def buscar_compromisso_por_id(self, id_compromisso: int) -> Optional[Compromisso]:
        conexao = self.db_connection.conectar()
        try:
            with conexao.cursor() as cursor:
                sql = "SELECT id_compromisso, id_categoria, titulo, descricao, data_inicio, data_fim, prioridade, status FROM compromisso WHERE id_compromisso = %s"
                cursor.execute(sql, (id_compromisso,))
                row = cursor.fetchone()
                if row:
                    return Compromisso(
                        id_compromisso=row['id_compromisso'],
                        id_categoria=row['id_categoria'],
                        titulo=row['titulo'],
                        descricao=row['descricao'],
                        data_inicio=row['data_inicio'],
                        data_fim=row['data_fim'],
                        prioridade=row['prioridade'],
                        status=row['status']
                    )
                return None
        finally:
            conexao.close()

    def atualizar_status_compromisso(self, id_compromisso: int, novo_status: str) -> Optional[Compromisso]:
        compromisso_atual = self.buscar_compromisso_por_id(id_compromisso)
        if not compromisso_atual:
            return None
        
        status_anterior = compromisso_atual.status
        
        conexao = self.db_connection.conectar()
        try:
            with conexao.cursor() as cursor:
                sql_update = "UPDATE compromisso SET status = %s WHERE id_compromisso = %s"
                cursor.execute(sql_update, (novo_status, id_compromisso))
                
                sql_hist = """
                    INSERT INTO historico (id_compromisso, status_anterior, status_novo, tipo_alteracao)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(sql_hist, (id_compromisso, status_anterior, novo_status, "Atualização de Status"))
                
                conexao.commit()
                
                compromisso_atual.status = novo_status
                return compromisso_atual
        finally:
            conexao.close()

    def listar_historicos(self) -> List[Historico]:
        conexao = self.db_connection.conectar()
        try:
            with conexao.cursor() as cursor:
                sql = "SELECT id_historico, id_compromisso, status_anterior, status_novo, data_alteracao, tipo_alteracao FROM historico"
                cursor.execute(sql)
                resultados = cursor.fetchall()
                return [
                    Historico(
                        id_historico=row['id_historico'],
                        id_compromisso=row['id_compromisso'],
                        status_anterior=row['status_anterior'],
                        status_novo=row['status_novo'],
                        data_alteracao=row['data_alteracao'],
                        tipo_alteracao=row['tipo_alteracao']
                    ) for row in resultados
                ]
        finally:
            conexao.close()