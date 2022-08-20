from clean_arch_python.enterprise.entities.client import Client
from clean_arch_python.infra.gateways.client_gateways import ClientInMemoryGateway


def test_find_all_should_return_a_copy_of_the___clients():
    client_inmemory_gateway = ClientInMemoryGateway()
    clients = client_inmemory_gateway.find_all()
    clients[0] = Client("Edited", "test", "test@mail.com", "12345678912")
    assert clients[0].first_name != client_inmemory_gateway.find_all()[0].first_name


def test_find_all_should_return_a_list_of_clients():
    client_inmemory_gateway = ClientInMemoryGateway()

    expected_clients = [
        Client("test", "test", "test@mail.com", "12345678912"),
    ]
    actual_clients = client_inmemory_gateway.find_all()

    assert len(actual_clients) == len(expected_clients)
    for actual_client, expected_client in zip(actual_clients, expected_clients):
        assert actual_client.first_name == expected_client.first_name
        assert actual_client.last_name == expected_client.last_name
        assert actual_client.email == expected_client.email
        assert actual_client.cpf == expected_client.cpf


def test_create_should_create_a_client():
    client_inmemory_gateway = ClientInMemoryGateway()

    clent_to_create = Client("new", "test", "new@mail.com", "12345678912")
    client_inmemory_gateway.create(clent_to_create)
    actual_clients = client_inmemory_gateway.find_all()

    assert len(actual_clients) == 2
    assert actual_clients[1].first_name == clent_to_create.first_name
    assert actual_clients[1].last_name == clent_to_create.last_name
    assert actual_clients[1].email == clent_to_create.email
    assert actual_clients[1].cpf == clent_to_create.cpf
