from clean_arch_python.infra.controllers import Controller
from clean_arch_python.infra.web.http import HttpRequest, HttpResponse, StatusCodes
from clean_arch_python.infra.presenters.client_presenters import (
    FindAllClientsOutputBoundary,
    CreateClientInputBoundary,
    CreateClientOutputBoundary,
)
from clean_arch_python.application.usecases.client_usecases import (
    FindAllClientsUseCase,
    CreateClientUseCase,
)


class FindAllClientsController(Controller):
    def __init__(self, findAllClientsUseCase: FindAllClientsUseCase) -> None:
        self.findAllClientsUseCase = findAllClientsUseCase

    def execute(self, request: HttpRequest) -> HttpResponse:
        clients = self.findAllClientsUseCase.execute()
        return HttpResponse(
            status_code=StatusCodes.OK,
            body=FindAllClientsOutputBoundary.to_json(clients),
        )


class CreateClientController(Controller):
    def __init__(self, createClientUseCase: CreateClientUseCase) -> None:
        self.createClientUseCase = createClientUseCase

    def execute(self, request: HttpRequest) -> HttpResponse:
        client_to_create = CreateClientInputBoundary.from_json(request.body)
        created_client = self.createClientUseCase.execute(client_to_create)
        return HttpResponse(
            status_code=StatusCodes.CREATED,
            body=CreateClientOutputBoundary.to_json(created_client),
        )
