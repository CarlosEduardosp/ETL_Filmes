from src.infra.connection import ConnectionDB



db = ConnectionDB()

colecao = db.conectardb()

# Testando a conexão inserindo um documento
documento_teste = {"mensagem": "terceira Conexão", "Data": "30/08/2024"}
resultado = colecao.insert_one(documento_teste)

print("Documento de teste inserido com o ID:", resultado.inserted_id)
