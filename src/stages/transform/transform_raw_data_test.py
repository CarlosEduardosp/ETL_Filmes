from src.stages.contracts.mocks.extract_contractMock import extract_contract_mock
from src.stages.contracts.tranform_contract import TranformContract
from src.errors.transform_error import TransformError
from .transform_raw_data import TransformRawData


def test_transform():
    transform_raw_data = TransformRawData()
    transformed_data_contract = transform_raw_data.transform(extract_contract_mock)

    print(transformed_data_contract.load_content)


    assert isinstance(transformed_data_contract, TranformContract)
    assert "nome" in transformed_data_contract.load_content[0]
    assert "url_imagem" in transformed_data_contract.load_content[0]
    assert "duracao" in transformed_data_contract.load_content[0]
    assert "categoria" in transformed_data_contract.load_content[0]
    assert "diretor" in transformed_data_contract.load_content[0]
    assert "atores" in transformed_data_contract.load_content[0]
    assert "avaliacao" in transformed_data_contract.load_content[0]
    assert "sinopse" in transformed_data_contract.load_content[0]
    assert "extraction_date" in transformed_data_contract.load_content[0]

def test_transform_error():
    transform_raw_data = TransformRawData()
    try:
        transform_raw_data.transform('entradaerrada')
    except Exception as exception: # pylint: disable=broad=except
        assert isinstance(exception, TransformError)
