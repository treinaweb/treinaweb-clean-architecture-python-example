from clean_arch_python.application.usecases.client_usecases import FindAllClientsUseCase
from clean_arch_python.infra.gateways.client_gateways import ClientInMemoryGateway


def test_find_all_clients_usecase():
    gateway = ClientInMemoryGateway()
    usecase = FindAllClientsUseCase(gateway)
    clients = usecase.execute()
    assert len(clients) == 1
    assert clients[0].first_name == "test"
    assert clients[0].last_name == "test"
    assert clients[0].email == "test@mail.com"
    assert clients[0].cpf == "12345678912"
