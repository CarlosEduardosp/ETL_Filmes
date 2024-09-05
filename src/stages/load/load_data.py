from src.infra.repositorio.interface_repositorio.interface_repositorio import InterfaceRepositorio
from src.stages.contracts.tranform_contract import TranformContract
from src.errors.load_error import LoadError


class LoadData:
    def __init__(self, repository: InterfaceRepositorio) -> None:
        self.repository = repository

    def Load(self, transformed_data_contract: TranformContract) -> None:
        print('chegou aqui')
        try:

            load_content = transformed_data_contract.load_content

            self.repository.insertData(load_content)

            return {"Success": True, "message": f'Inserção de {len(load_content)} dados, Realizada com Sucesso'}

        except Exception as exception:
            raise LoadError(str(exception)) from exception
