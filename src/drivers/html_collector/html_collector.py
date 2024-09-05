# pylint: disable=W0105, W0221
"""
Arquivo html_collector
"""
from typing import List
from bs4 import BeautifulSoup
from src.drivers.interfaces.html_collector_interface import HtmlCollectorInterface
"""
Classe HtmlCollector
"""


class HtmlCollector(HtmlCollectorInterface):
    """
    classe HTMLCollector
    """

    @classmethod
    def collect_essential_information(cls, html: str) -> List:
        """
        :param html:
        :return:
        """

        soup = BeautifulSoup(html, 'html.parser')

        response = soup.find_all('li', class_="mdl")

        lista_filmes = []
        for i in response:

            nome_filme = i.find('a', {'class': 'meta-title-link'}).contents[0]
            url_imagem = i.find('img', {'class': 'thumbnail-img'})['src']
            duracao = i.find('div', {'class': 'meta-body-item meta-body-info'}).contents[0]

            categorias = i.find('div', {'class': 'meta-body-item meta-body-info'})
            categoria = categorias.find_all('span', {'class': 'dark-grey-link'})
            generos = []
            for j in categoria:
                generos.append(j.get_text(strip=True))

            diretores = i.find('div', {'class': 'meta-body-item meta-body-direction'})
            direcao = diretores.find_all('span', {'class': 'dark-grey-link'})
            diretor = []
            for j in direcao:
                diretor.append(j.get_text(strip=True))

            elenco = i.find('div', {'class': 'meta-body-item meta-body-actor'})
            ator = elenco.find_all('a', {'class': 'dark-grey-link'})
            atores = []
            for j in ator:
                atores.append(j.get_text(strip=True))

            avaliacao = i.find('span', {'class': 'stareval-note'}).contents[0]

            sinopse = i.find('div', {'class': 'content-txt'}).contents[0]

            filme = {
                "nome": nome_filme,
                "url_imagem": url_imagem,
                "duracao": duracao,
                "categoria": generos,
                "diretor": diretor,
                "atores": atores,
                "avaliacao": avaliacao,
                "sinopse": sinopse
            }
            lista_filmes.append(
                filme
            )

        return lista_filmes