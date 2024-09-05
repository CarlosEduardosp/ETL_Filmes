"""
Módulo para realizar o GET dos dados.
"""
from typing import Dict
import requests
from src.drivers.interfaces.http_requester_interface import HttpRequesterInterface


class HttpRequester(HttpRequesterInterface):
    """
    Classe HttpRequester.
    """

    def __init__(self) -> None:
        """
        Método construtor com a URL da requisição.
        """
        self.__url = ('https://www.adorocinema.com/filmes/melhores/?page=13') # o numero que está em page={numero} já foi realizado o requeste.

    def request_from_page(self) -> Dict:
        """
        Realiza uma requisição GET na URL desejada e retorna um dicionário com os dados.

        :return: Dicionário com dados do GET na URL desejada.
        """
        response = requests.get(self.__url, timeout=10)
        return {
            "status_code": response.status_code,
            "html": response.text
        }
