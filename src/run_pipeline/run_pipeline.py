from src.stages.extract.extract_html import ExtractHtml
from src.stages.transform.transform_raw_data import TransformRawData
from src.stages.load.load_data import LoadData
from src.drivers.html_collector.html_collector import HtmlCollector
from src.drivers.http_requester.http_requester import HttpRequester
from src.infra.repositorio.filmesrepositorio import FilmesRepositorio


class MainPipeline:
    def __init__(self) -> None:
        self.__extract_html = ExtractHtml(HttpRequester(), HtmlCollector())
        self.__tranform_raw_data = TransformRawData()
        self.__load_data = LoadData(FilmesRepositorio())

    def run_pipeline(self) -> None:
        extract_contract = self.__extract_html.extract()
        tranformed_data_contract = self.__tranform_raw_data.transform(extract_contract)
        self.__load_data.Load(tranformed_data_contract)



