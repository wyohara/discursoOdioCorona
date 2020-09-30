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

    def realizar_pesquisa(self, query="", result_type="mixed", lang="pt", count=100):
        """
        Método responsável por realizar a pesquisa no tweepy
        :param query:
        :param result_type:
        :param lang:
        :return:
        """

        # criando a query para pesquisa no tweepy
        public_tweets = self.__api.search(query,
                                          lang=lang,
                                          result_type=result_type,
                                          count=count)
        # percorrendo os resultados
        for tweet in public_tweets:
            try:  # tenta salvar os dados
                Database().salvar_tweets_discurso_odio(tweet._json)
            except tweepy.RateLimitError:  # caso o limite de consultas tenha sido alcançado
                print('[*] Pausando o tweepy por 1 minuto')
                time.sleep(60)
            except tweepy.error.TweepError:  # caso ocorra algum erro no tweepy
                print("[*] Falha ao executar o comando no tweepy, saindo...")


if __name__ == '__main__':
    DownloadDados_tweepy().realizar_pesquisa('china OR sinovac (vacina OR covid OR corona OR pandemia OR sinovac)')
