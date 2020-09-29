import tweepy
import json
from dotenv import load_dotenv
import os
import time
from database.Database import Database

class DownloadDados_tweepy(object):
    def __init__(self):
        load_dotenv()
        auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_KEY_SECRET"))
        auth.set_access_token(os.getenv("ACESS_TOKEN"), os.getenv("ACESS_TOKEN_SECRET"))

        # criando a chave de acesso da api
        # parser é o parser que retorna os dados como um json
        # self.__api = tweepy.API(auth, parser=tweepy.parsers.JSONParser()) # converte em json
        self.__api = tweepy.API(auth)

    def realizar_pesquisa(self, query="", result_type="popular", lang="pt", count=100):
        """
        Método responsável por realizar a pesquisa no tweepy
        :param query:
        :param result_type:
        :param lang:
        :return:
        """
        public_tweets = self.__api.search(query,
                                          lang=lang,
                                          result_type=result_type,
                                          count=count)
        # #formatando para string
        # result_formatted = json.dumps(public_tweets, indent=4, sort_keys=True)
        # print(json.loads(result_formatted.encode('UTF-8')))

        print('map result')
        for tweet in public_tweets:
            try:
                print(tweet._json)
                Database().salvar_tweets_discurso_odio(tweet._json)
                break
            except tweepy.RateLimitError:
                print('sleep 1 minute')
                time.sleep(60)
            except tweepy.error.TweepError:
                print("Failed to run the command on that user, Skipping...")


if __name__ == '__main__':
    DownloadDados_tweepy().realizar_pesquisa('china(covid OR corona)', count=100)
