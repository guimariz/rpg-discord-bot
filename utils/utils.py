from pymongo import MongoClient

# Conectar ao MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Criar/Selecionar o banco de dados
db = client['tis-rpg_database']

# Criar/Selecionar a coleção
rpg_collection = db['rpgs']

# Inserir um documento para garantir que a coleção e o banco de dados sejam criados
rpg_collection.insert_one({
    'nome_rpg': 'Exemplo RPG',
    'cenas': [{'cena1': []},],
    'template_fichas': 12314,
    'chat_gameplay': False,
    'mestre': 123456789
})

print("Banco de dados e coleção criados com sucesso!")
