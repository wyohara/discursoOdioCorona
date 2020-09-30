from pymongo import MongoClient
from bson.objectid import ObjectId

"""
Para iniciar o mongodb usa = sudo systemctl restart mongod
"""


class Database(object):
    def __init__(self):
        self.__client = MongoClient('mongodb://localhost:27017/')
        self.COL_TWEETS = "tweets"
        self.__db = self.__client["tweets_discurso_odio"]

    def salvar_tweets_discurso_odio(self, tweet):
        coll = self.__db[self.COL_TWEETS]  # selecionando o banco da collection
        # verificando se o id do tweet já existe no banco de dados
        if coll.find_one({'id': tweet['id']}) is None:  # caso não exista o twee é salvo no banco
            inserted_id = coll.insert_one(tweet).inserted_id
            print('[*] inserido tweet com _id %s' % inserted_id)
        else:  # caso exista um tweet com mesmo id ele é ignorado
            # print('[*] tweet com id %s já existe no banco de dados' % tweet['id'])
            pass

    def recperar_tweet(self, id_selected=None):
        coll = self.__db[self.COL_TWEETS]  # selecionando o banco da collection
        if id_selected is None:
            return coll.find_one()
        else:
            return coll.find_one({'id': id_selected})

    def busca_geral_tweet(self, query=None):
        coll = self.__db[self.COL_TWEETS]  # selecionando o banco da collection
        if query is None:
            return coll.find_one()
        else:
            return coll.find(query)

    def buscar_todos_tweet(self):
        coll = self.__db[self.COL_TWEETS]  # selecionando o banco da collection
        return coll.find({})

    def deletar_tweet(self, _id_mongo):
        col = self.__db[self.COL_TWEETS]
        print(col.delete_one({'_id': ObjectId(_id_mongo)}))
        print("[*] arquivo deletado")


if __name__ == '__main__':
    Database().salvar_tweets_discurso_odio({"a": 1})
