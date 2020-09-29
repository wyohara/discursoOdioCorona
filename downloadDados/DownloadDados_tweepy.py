import tweepy
import json
from dotenv import load_dotenv
import os

class DownloadDados_tweepy(object):
    def __init__(self):
        load_dotenv()
        auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_KEY_SECRET"))
        auth.set_access_token(os.getenv("ACESS_TOKEN"), os.getenv("ACESS_TOKEN_SECRET"))

        #criando a chave de acesso da api
        #parser é o parser que retorna os dados como um json
        self.__api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    def realizar_pesquisa(self):
        public_tweets = self.__api.search('china (corona OR coronavirus)',
                                          lang="pt",
                                          result_type="popular")
        result_formatted = json.dumps(public_tweets, indent=4, sort_keys=True)
        print (result_formatted)


if __name__ == '__main__':
    DownloadDados_tweepy().realizar_pesquisa()