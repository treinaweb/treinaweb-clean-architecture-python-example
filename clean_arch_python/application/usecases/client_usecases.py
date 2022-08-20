from typing import List

from clean_arch_python.enterprise.entities.client import Client
from clean_arch_python.application.gateways.client_gateways import ClientGateway


class FindAllClientsUseCase:
    def __init__(self, client_gateway: ClientGateway):
        self.__client_gateway = client_gateway

    def execute(self) -> List[Client]:
        return self.__client_gateway.find_all()


class CreateClientUseCase:
    def __init__(self, client_gateway: ClientGateway):
        self.__client_gateway = client_gateway

    def execute(self, client: Client) -> Client:
        self.__client_gateway.create(client)
        return client
