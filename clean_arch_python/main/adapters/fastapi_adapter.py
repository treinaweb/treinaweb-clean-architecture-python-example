from typing import Callable
from fastapi import Response, Request

from clean_arch_python.infra.controllers import Controller
from clean_arch_python.infra.web.http import HttpRequest


class FastAPIAdapter:
    @staticmethod
    def adapt(controller: Controller) -> Callable[[Request], Response]:
        async def handle_request(request: Request) -> Response:
            body = await request.body()
            response = controller.execute(HttpRequest(body))
            return Response(response.body, response.status_code)

        return handle_request
