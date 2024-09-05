from src.infra.connection import ConnectionDB

db = ConnectionDB()

colecao = db.conectardb()

# Filtro para identificar o documento a ser atualizado
filtro = {"mensagem": "terceira Conexão"}

# Novo campo a ser adicionado
novo_campo = {"$set": {"status": True}}

# Adicionando o novo campo
resultado = colecao.update_one(filtro, novo_campo)

# Verificando se o documento foi modificado
if resultado.modified_count > 0:
    print("Campo adicionado com sucesso!")
else:
    print("Nenhum documento encontrado com esse filtro.")