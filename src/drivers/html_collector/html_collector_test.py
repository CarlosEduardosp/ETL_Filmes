# pylint: disable=W9008
"""
html_collector_test
"""
from src.drivers.html_collector.html_collector import HtmlCollector
from src.drivers.mocks.http_requester_mock import mock_request_from_page
from src.drivers.http_requester.http_requester import HttpRequester


def test_collect_essential_information():
    """
    :return: print
    """
    # utilizando o html mock
    http_request_response = mock_request_from_page()

    html_collector = HtmlCollector()
    essential_information = html_collector.collect_essential_information(http_request_response['html'])
    print(essential_information)
    assert isinstance(essential_information, list)
    assert isinstance(essential_information[0], dict)
    assert 'nome' in essential_information[0]
    assert 'url_imagem' in essential_information[0]


def test_collect_essencial_information():
    requester = HttpRequester()
    resquester_response = requester.request_from_page()

    html_collector = HtmlCollector()
    essential_information = html_collector.collect_essential_information(resquester_response['html'])


