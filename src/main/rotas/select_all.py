from fastapi import APIRouter
from src.infra.repositorio.filmesrepositorio import FilmesRepositorio

router = APIRouter()


@router.get("/")
def select_all():
    """
    :return: Realiza o select de todos os dados, salvos com o run_pipeline, do banco de dados.
    """
    select = FilmesRepositorio()

    data_response = select.select()

    response = {
        "Success": 200,
        "Message": "O objetivo desta API é coletar dados de uma página web, transformá-los e salvá-los em um banco de dados MongoDB na nuvem,"
                   " além de disponibilizar um endpoint para acessar esses dados.",
        "Info": (
            "Esta API oferece dados coletados utilizando técnicas de web scraping e ETL (Extract, Transform, Load). "
            "Os dados são extraídos da URL: https://www.adorocinema.com/filmes/melhores/?page=1. "
            "Em seguida, são transformados para o formato desejado, corrigindo informações e selecionando os dados relevantes. "
            "Posteriormente, esses dados são salvos em um banco de dados MongoDb na nuvem, utilizando a plataforma Atlas para melhor visualização."
        ),
        "Arquitetura": (
            "A arquitetura limpa foi adotada para garantir a separação de responsabilidades, a testabilidade e a facilidade de manutenção. "
            "O projeto é estruturado em várias camadas, incluindo camadas de drivers, extração (extract), transformação (transform) e carregamento (load). "
            "Cada camada é responsável por uma parte específica do processo ETL, assegurando que cada componente tenha uma única responsabilidade."
        ),
        "Bibliotecas Principais": (
            "As principais bibliotecas utilizadas no projeto são: "
            "FastAPI para a criação de APIs web rápidas e eficientes, "
            "Pytest para a criação e execução de testes unitários, "
            "BeautifulSoup para a realização de web scraping, e "
            "Requests para fazer requisições HTTP."
            "Pymongo para interação com o banco de dados MongoDB"
        ),
        "Padrões de Design": (
            "O projeto segue vários padrões de design para garantir a escalabilidade e a manutenibilidade do código. "
            "O Repository Pattern é utilizado para abstrair a camada de acesso a dados, facilitando a troca de implementações de banco de dados sem impactar outras partes do sistema. "
            "A Dependency Injection é utilizada para gerenciar dependências, permitindo a fácil substituição de componentes e melhorando a testabilidade do código."
        ),
        "Boas Práticas": (
            "Boas práticas de desenvolvimento foram seguidas durante a implementação do projeto, incluindo: "
            "escrita de testes unitários para garantir a funcionalidade correta dos componentes, "
            "adoção dos princípios SOLID para um design de software robusto e flexível, e "
            "uso de ferramentas de linting e formatação de código para manter a consistência e a qualidade do código."
        ),
        "Documentação": "Utilize '(link)/docs' para acessar a documentação completa via Swagger, que fornece uma interface interativa para explorar e testar os endpoints da API.",
        "Desenvolvedor": "Carlos Eduardo dos S. Padilha",
        "Quantidade_filmes": f"{len(data_response)}",
        "dados": {"Todos os filmes salvos": data_response}
    }

    return response
