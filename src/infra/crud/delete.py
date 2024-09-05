from src.infra.connection import ConnectionDB

db = ConnectionDB()

colecao = db.conectardb()

# Filtro para identificar os documentos a serem atualizados
filtro = {"mensagem": "terceira Conexão"}

# Atualizando múltiplos documentos
resultado = colecao.delete_one(filtro)

# Exibindo o número de documentos modificados
print("Número de documentos atualizados:", resultado.deleted_count)