from typing import Dict
from abc import ABC, abstractmethod
from src.stages.contracts.tranform_contract import TranformContract


class InterfaceRepositorio(ABC):
    """
    Classe HttpRequester.
    """
    @abstractmethod
    def insertData(self, dataloadcontent: TranformContract) -> str:
        pass

    @abstractmethod
    def select(self):
        pass