from pymongo import MongoClient


class ConnectionDB:

    def __init__(self):

        # URL de conexão fornecida pelo MongoDB Atlas
        # Substitua "<your-cluster-url>" pelo seu URL real. Normalmente, ele se parece com 'cluster0.mongodb.net'.
        self.__url_conexao = "mongodb+srv://guitarristas2004:EzlSVlyCrTxMfEKe@cluster0.wi3ae.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

        # Criando uma instância de MongoClient e conectando-se ao cluster
        self.__client = MongoClient(self.__url_conexao)

    def conectardb(self):

        # Selecionando o banco de dados (crie ou use um banco existente)
        db = self.__client['banco_etl_filmes']

        # Selecionando uma coleção
        colecao = db['meus_filmes']

        return colecao



