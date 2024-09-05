from src.infra.connection import ConnectionDB

db = ConnectionDB()

colecao = db.conectardb()

resultado = colecao.find()

for i in resultado:
    print(i)
