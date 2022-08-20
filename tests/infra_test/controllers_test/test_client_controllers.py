from clean_arch_python.infra.controllers.client_controllers import (
    FindAllClientsController,
)
from clean_arch_python.infra.web.http import HttpRequest, HttpResponse, StatusCodes
from clean_arch_python.infra.gateways.client_gateways import ClientInMemoryGateway
from clean_arch_python.application.usecases.client_usecases import FindAllClientsUseCase


def test_find_all_clients_controller():
    gateway = ClientInMemoryGateway()
    usecase = FindAllClientsUseCase(gateway)
    controller = FindAllClientsController(usecase)

    expected_response = HttpResponse(
        StatusCodes.OK,
        '[{"first_name": "test", "last_name": "test", "email": "test@mail.com", "cpf": "12345678912"}]',
    )
    actual_response = controller.execute(HttpRequest(""))

    assert actual_response.status_code == expected_response.status_code
    assert actual_response.body == expected_response.body
