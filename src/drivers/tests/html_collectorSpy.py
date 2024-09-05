# pylint: disable=W0105, W0221, C0103
"""
Arquivo html_collector
"""
from typing import List
"""
Classe HtmlCollector
"""


class HtmlCollectorSPY:
    """
    classe HTMLCollector
    """

    def __init__(self) -> None:
        self.collect_essential_information_attribuites = {}

    def collect_essential_information(self, html: str) -> List:
        """
        :param html:
        :return:
        """
        self.collect_essential_information_attribuites['html'] = html
        return [{
            "nome": "somename",
                "url_imagem": 'someurl',
                "duracao": 'someduração',
                "categoria": 'somecategoria',
                "diretor": 'somediretor',
                "atores": 'someatores',
                "avaliacao": 'someavaliação',
                "sinopse": 'somesinopse'
        }]
