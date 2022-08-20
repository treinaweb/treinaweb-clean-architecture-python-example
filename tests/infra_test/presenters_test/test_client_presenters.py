from clean_arch_python.enterprise.entities.client import Client
from clean_arch_python.infra.presenters.client_presenters import (
    FindAllClientsOutputBoundary,
    CreateClientInputBoundary,
    CreateClientOutputBoundary,
)


def test_find_all_all_clients_output_boundary_to_json():
    clients = [Client("test", "test", "test@mail.com", "12345678912")]
    expected_json = '[{"first_name": "test", "last_name": "test", "email": "test@mail.com", "cpf": "12345678912"}]'
    json = FindAllClientsOutputBoundary.to_json(clients)
    assert json == expected_json


def test_find_all_all_clients_output_boundary_to_json_empty():
    clients = []
    expected_json = "[]"
    json = FindAllClientsOutputBoundary.to_json(clients)
    assert json == expected_json


def test_find_all_all_clients_output_boundary_to_json_none():
    clients = None
    expected_json = "[]"
    json = FindAllClientsOutputBoundary.to_json(clients)
    assert json == expected_json


def test_create_client_input_boundary_from_json():
    json_data = '{"first_name": "test", "last_name": "test", "email": "test@mail.com", "cpf": "12345678912"}'
    expected_client = Client("test", "test", "test@mail.com", "12345678912")
    actual_client = CreateClientInputBoundary.from_json(json_data)
    assert actual_client.first_name == expected_client.first_name
    assert actual_client.last_name == expected_client.last_name
    assert actual_client.email == expected_client.email
    assert actual_client.cpf == expected_client.cpf


def test_create_client_output_boundary_to_json():
    client = Client("test", "test", "test@mail.com", "12345678912")
    expected_json = '{"first_name": "test", "last_name": "test", "email": "test@mail.com", "cpf": "12345678912"}'
    actual_json = CreateClientOutputBoundary.to_json(client)
    assert actual_json == expected_json


def test_create_client_output_boundary_to_json_none():
    client = None
    expected_json = "{}"
    actual_json = CreateClientOutputBoundary.to_json(client)
    assert actual_json == expected_json
