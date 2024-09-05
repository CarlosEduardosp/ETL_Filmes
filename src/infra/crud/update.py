from src.infra.connection import ConnectionDB

db = ConnectionDB()

colecao = db.conectardb()

# Filtro para identificar os documentos a serem atualizados
filtro = {"mensagem": "Engenheiro de Dados"}

# Nova informação a ser atualizada
nova_informacao = {"$set": {"mensagem": "Engenheiro de Dados"}}

# Atualizando múltiplos documentos
resultado = colecao.update_many(filtro, nova_informacao)

# Exibindo o número de documentos modificados
print("Número de documentos atualizados:", resultado.modified_count)