from typing import List, Dict
from src.stages.contracts.extract_contract import ExtractContract
from src.stages.contracts.tranform_contract import TranformContract
from src.errors.transform_error import TransformError


class TransformRawData:

    def transform(self, extract_contract: ExtractContract) -> TranformContract:
        try:
            transform_information = self.__filter_and_transform_data(extract_contract)
            transformed_data_contract = TranformContract(
                load_content=transform_information
            )
            return transformed_data_contract

        except Exception as exception:
            raise TransformError(str(exception)) from exception

    def __filter_and_transform_data(self, extract_contract: ExtractContract) -> List:
        extract_date = extract_contract.extraction_date
        data_content = extract_contract.raw_informatiom_content
        transform_information = []

        for data in data_content:
            data['duracao'] = data['duracao'].strip()
            data['avaliacao'] = data['avaliacao'].strip()
            data['sinopse'] = data['sinopse'].strip()

            lista_atores = []

            # Verifica a quantidade de atores
            num_atores = len(data['atores'])

            if num_atores == 1:
                pass  # Apenas um ator, nenhum processamento adicional é necessário

            # Tratamento para dois ou mais atores
            elif num_atores >= 2:
                # Garante o processamento de no máximo 2 atores
                for i in range(min(2, num_atores)):
                    ator = data['atores'][i].split()
                    ator_data = {}

                    # Verifica a quantidade de nomes dos atores
                    if len(ator) == 1:
                        ator_data = {
                            "first_name": ator[0]
                        }
                    elif len(ator) == 2:
                        ator_data = {
                            "first_name": ator[0],
                            "second_name": ator[1]
                        }
                    elif len(ator) == 3:
                        ator_data = {
                            "first_name": ator[0],
                            "second_name": ator[1],
                            "third_name": ator[2]
                        }

                    # Salva os dados do ator na lista de atores
                    actor_label = f"actor_{'one' if i == 0 else 'two'}"
                    lista_atores.append({actor_label: ator_data})

            data['atores'] = lista_atores

            # Dividindo os nomes dos diretores
            lista_diretores = []
            num_diretores = len(data['diretor'])

            # Garante que só processaremos no máximo 2 diretores
            for i in range(min(2, num_diretores)):
                full_name = data['diretor'][i].split()
                # Garante que há pelo menos um nome e um sobrenome
                if len(full_name) >= 2:
                    diretor_data = {
                        "first_name": full_name[0],
                        "second_name": full_name[1]
                    }
                    director_label = f"director_{'one' if i == 0 else 'two'}"
                    lista_diretores.append({director_label: diretor_data})

            data['diretor'] = lista_diretores

            transform_information.append(data)

            for i in transform_information:
                i["extraction_date"] = extract_date

        return transform_information


    def __transform_data(self, data):

        return data
