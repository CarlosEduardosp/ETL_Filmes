from src.stages.contracts.mocks.extract_contractMock import extract_contract_mock
from src.stages.contracts.tranform_contract import TranformContract
from src.errors.transform_error import TransformError
from src.stages.transform.transform_raw_data import TransformRawData
from src.stages.load.load_data import LoadData
from src.infra.repositorio.filmesrepositorio import FilmesRepositorio


def test_insert_load():
    transform_raw_data = TransformRawData()
    transformed_data_contract = transform_raw_data.transform(extract_contract_mock)

    repo = FilmesRepositorio()
    load = LoadData(repo)
    response = load.Load(transformed_data_contract)

    print(response)

