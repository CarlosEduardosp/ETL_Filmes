from pymongo import MongoClient
import ssl

class ConnectionDB:

    def __init__(self):

        # URL de conexão fornecida pelo MongoDB Atlas
        # Substitua "<your-cluster-url>" pelo seu URL real. Normalmente, ele se parece com 'cluster0.mongodb.net'.
        #self.__url_conexao = "mongodb+srv://guitarristas2004:EzlSVlyCrTxMfEKe@cluster0.wi3ae.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        self.__url_conexao = "mongodb+srv://guitarristas2004:EzlSVlyCrTxMfEKe@cluster0.wi3ae.mongodb.net/?retryWrites=true&w=majority&tls=true"

        # Criando uma instância de MongoClient e conectando-se ao cluster
        self.__client = MongoClient(self.__url_conexao, tls=True, tlsAllowInvalidCertificates=True)

    def conectardb(self):

        # Selecionando o banco de dados (crie ou use um banco existente)
        db = self.__client['banco_etl_filmes']

        # Selecionando uma coleção
        colecao = db['meus_filmes']

        return colecao



