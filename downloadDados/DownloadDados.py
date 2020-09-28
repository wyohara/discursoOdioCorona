from dotenv import load_dotenv
import os
import requests
import json

"""
Criado em 28/09/2020
"""


class DownloadDados(object):
    def __init__(self):
        """
        Classe responsável por realizar uma busca dos termos no twitter
        """
        # carregando os dados no .env que serão usados
        load_dotenv()
        BEARED_TOKEN = os.getenv("BEARER_TOKEN_TWITTER")
        self.__headers = {"Authorization": "Bearer {}".format(BEARED_TOKEN)}

    def pesquisarTweet(self, termo=""):
        """
        Método que retorna os tweets relacionados a um termo
        :param termo: Termo chave da pesquisa
        :return: JSON de dados
        """
        query = 'keyword="eleição"'
        tweet_fields = "tweet.fields=attachments,author_id,context_annotations,conversation_id,created_at,entities," \
                       "geo,id,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,source," \
                       "text,withheld"
        maxResults="max_results=100"
        url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}&{}".format(
            query, tweet_fields, maxResults
        )

        response = requests.request("GET", url, headers=self.__headers)
        print("Status Code: %s" % response.status_code)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)

        return json.dumps(response.json(), indent=4, sort_keys=True)


if __name__ == '__main__':
    result = DownloadDados().pesquisarTweet()
    print (result)
