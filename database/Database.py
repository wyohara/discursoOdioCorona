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
        col = self.__db[self.COL_TWEETS]  # selecionando o banco da collection
        # verificando se o id do tweet já existe no banco de dados
        if col.find_one({'id': tweet['id']}) is None: # caso não exista o twee é salvo no banco
            inserted_id = col.insert_one(tweet).inserted_id
            print('[*] inserido tweet com _id %s' % inserted_id)
        else: # caso exista um tweet com mesmo id ele é ignorado
            # print('[*] tweet com id %s já existe no banco de dados' % tweet['id'])
            pass

    def deletar_tweet(self, id):
        col = self.__db[self.COL_TWEETS]
        print(col.delete_one({'_id': ObjectId(id)}))
        print("[*] arquivo deletado")


if __name__ == '__main__':
    Database().salvar_tweets_discurso_odio({"a": 1})
