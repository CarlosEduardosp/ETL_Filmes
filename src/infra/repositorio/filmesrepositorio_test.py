from src.infra.repositorio.filmesrepositorio import FilmesRepositorio
from src.stages.transform.transform_raw_data import TransformRawData
from src.stages.contracts.mocks.extract_contractMock import extract_contract_mock

def test_inserir():

    repo = FilmesRepositorio()

    transform_data = TransformRawData()

    transform_data_contract = transform_data.transform(extract_contract_mock)

    response = repo.insertData(dataloadcontent=transform_data_contract.load_content)

    print(response)


def testselect():

    repo = FilmesRepositorio()

    response = repo.select()

    #print(response)

