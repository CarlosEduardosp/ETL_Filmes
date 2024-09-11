from pymongo import MongoClient
import os

class ConnectionDB:

    def __init__(self):
        # URL de conexão fornecida pelo MongoDB Atlas
        # Substitua as credenciais por variáveis de ambiente para maior segurança
        username = os.getenv('MONGO_USERNAME', 'guitarristas2004')
        password = os.getenv('MONGO_PASSWORD', 'EzlSVlyCrTxMfEKe')
        cluster_url = "cluster0.wi3ae.mongodb.net"

        # URL de conexão segura com variáveis de ambiente
        self.__url_conexao = f"mongodb+srv://{username}:{password}@{cluster_url}/?retryWrites=true&w=majority"

        # Criando uma instância de MongoClient e conectando-se ao cluster
        self.__client = MongoClient(
            self.__url_conexao,
            tls=True,
            tlsAllowInvalidCertificates=False  # Use isso apenas se for absolutamente necessário
        )

    def conectardb(self):
        # Selecionando o banco de dados (crie ou use um banco existente)
        db = self.__client['banco_etl_filmes']

        # Selecionando uma coleção
        colecao = db['meus_filmes']

        return colecao
