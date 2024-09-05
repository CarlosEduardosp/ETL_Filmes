"""
arquivo de teste
"""
from requests_mock import Mocker
from src.drivers.http_requester.http_requester import HttpRequester


def test_request_from_page(requests_mock: Mocker) -> None:
    """
    Testa o método request_from_page da classe HttpRequester.

    :param requests_mock: modulo request_mock

    """
    url = 'https://www.adorocinema.com/filmes/melhores/?page=1'
    response_context = '<h1>Ola Mundo</h1>'
    requests_mock.get(url, status_code=200, text=response_context)

    http_request = HttpRequester()
    request_response = http_request.request_from_page()

    assert 'status_code' in request_response
    assert 'html' in request_response
    assert request_response['status_code'] == 200
    assert request_response['html'] == response_context


def test_request_from_page():

    http_request = HttpRequester()
    request_response = http_request.request_from_page()
    print(request_response['html'])
