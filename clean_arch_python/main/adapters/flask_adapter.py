from typing import Callable, Tuple
from flask import request

from clean_arch_python.infra.controllers import Controller
from clean_arch_python.infra.web.http import HttpRequest


class FlaskAdapter:
    @staticmethod
    def adapt(controller: Controller) -> Callable[[], Tuple[str, int]]:
        def handle_request() -> Tuple[str, int]:
            response = controller.execute(HttpRequest(request.get_data()))
            return response.body, response.status_code

        return handle_request
