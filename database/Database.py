from pymongo import MongoClient

"""
Para iniciar o mongodb usa = sudo systemctl restart mongod
"""
class Database(object):
    def __init__(self):
        self.__client = MongoClient('mongodb://localhost:27017/')

    def salvar_tweets_discurso_odio(self, tweet):
        db = self.__client.tweets_discurso_odio
        id=db.insert(tweet).inserted_id
        print(id)


if __name__ == '__main__':
    Database().salvar_tweets_discurso_odio({"a":1})
