from src.infra.connection import ConnectionDB
from src.stages.contracts.tranform_contract import TranformContract


class FilmesRepositorio:

    def __init__(self):
        self.db = ConnectionDB()
        self.colecao = self.db.conectardb()

    def insertData(self, dataloadcontent: TranformContract) -> str:

        try:

            for data in dataloadcontent:

                # Testando a conexão inserindo um documento
                documento = {
                    "nome": data['nome'],
                    "url_imagem": data['url_imagem'],
                    "duracao": data['duracao'],
                    "categoria": data['categoria'],
                    "diretor": data['diretor'],
                    "atores": data['atores'],
                    "avaliacao": data['avaliacao'],
                    "sinopse": data['sinopse'],
                    "extraction_date": f"{data['extraction_date']}"
                }
                resultado = self.colecao.insert_one(documento)

            return "Dados Inseridos com Sucesso"

        except:
            raise ValueError('Houve um erro')

    def select(self):

        resultado = self.colecao.find()

        if resultado:
            response = []
            for data in resultado:

                # print(type(data['_id']))
                data['_id'] = str(data['_id'])
                # print(type(data['_id']))
                response.append(data)

            return response

        else:
            return 'vazio'
