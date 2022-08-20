import abc

from clean_arch_python.infra.web.http import HttpRequest, HttpResponse


class Controller(abc.ABC):
    @abc.abstractmethod
    def execute(self, request: HttpRequest) -> HttpResponse:
        ...
