import psycopg2
from psycopg2 import sql
import sys
import os

class ConexaoDB:
    """Gerencia a conexão com o banco de dados PostgreSQL Netflix"""
    
    def __init__(self, 
                 host=None, 
                 user=None, 
                 password=None, 
                 database=None, 
                 port=5432):
        # Usar variáveis de ambiente se não especificadas
        self.host = host or os.getenv('PGHOST')
        self.user = user or os.getenv('PGUSER', 'postgres')
        self.password = password or os.getenv('PGPASSWORD', '')
        self.database = database or os.getenv('PGDATABASE', 'netflix')
        self.port = port
        self.conexao = None
        self.cursor = None
    
    def conectar(self):
        """Estabelece conexão com o banco de dados"""
        try:
            # Construir dicionário de conexão apenas com valores não-None
            conn_params = {
                'user': self.user,
                'database': self.database,
                'password': self.password
            }
            
            if self.host:
                conn_params['host'] = self.host
                conn_params['port'] = self.port
            
            self.conexao = psycopg2.connect(**conn_params)
            self.cursor = self.conexao.cursor()
            print("✅ Conexão com banco de dados estabelecida!")
            return True
        except psycopg2.OperationalError as e:
            print(f"❌ Erro ao conectar ao banco: {e}")
            return False
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            return False
    
    def desconectar(self):
        """Fecha a conexão com o banco"""
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()
            print("✅ Conexão fechada!")
    
    def executar(self, query, params=None):
        """Executa uma query e retorna o resultado"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conexao.commit()
            return True
        except psycopg2.Error as e:
            self.conexao.rollback()
            print(f"❌ Erro ao executar query: {e}")
            return False
    
    def buscar_um(self, query, params=None):
        """Retorna um resultado"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchone()
        except psycopg2.Error as e:
            print(f"❌ Erro ao buscar dados: {e}")
            return None
    
    def buscar_todos(self, query, params=None):
        """Retorna todos os resultados"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except psycopg2.Error as e:
            print(f"❌ Erro ao buscar dados: {e}")
            return []
    
    def obter_ultimo_id(self):
        """Retorna o último ID inserido"""
        try:
            self.cursor.execute("SELECT lastval();")
            resultado = self.cursor.fetchone()
            return resultado[0] if resultado else None
        except psycopg2.Error as e:
            print(f"❌ Erro ao obter último ID: {e}")
            return None
