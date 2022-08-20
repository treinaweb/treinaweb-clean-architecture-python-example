from clean_arch_python.application.gateways.client_gateways import ClientGateway
from clean_arch_python.application.usecases.client_usecases import (
    FindAllClientsUseCase,
    CreateClientUseCase,
)
from clean_arch_python.infra.controllers.client_controllers import (
    FindAllClientsController,
    CreateClientController,
)
from clean_arch_python.infra.gateways.client_gateways import ClientMySQLGateway


class ClientFactory:
    __gateway: ClientGateway = None

    @staticmethod
    def get_client_gateway() -> ClientGateway:
        if ClientFactory.__gateway is None:
            ClientFactory.__gateway = ClientMySQLGateway()
        return ClientFactory.__gateway

    @staticmethod
    def get_find_all_clients_usecase() -> FindAllClientsUseCase:
        return FindAllClientsUseCase(ClientFactory.get_client_gateway())

    @staticmethod
    def get_create_client_usecase() -> CreateClientUseCase:
        return CreateClientUseCase(ClientFactory.get_client_gateway())

    @staticmethod
    def get_find_all_clients_controller() -> FindAllClientsController:
        return FindAllClientsController(ClientFactory.get_find_all_clients_usecase())

    @staticmethod
    def get_create_client_controller() -> CreateClientController:
        return CreateClientController(ClientFactory.get_create_client_usecase())
