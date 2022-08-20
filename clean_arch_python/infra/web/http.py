from enum import Enum


class StatusCodes(Enum):
    OK = 200
    CREATED = 201


class HttpRequest:
    def __init__(self, body: str):
        self.__body = body

    @property
    def body(self) -> str:
        return self.__body


class HttpResponse:
    def __init__(self, status_code: StatusCodes, body: str):
        self.__status_code = status_code
        self.__body = body

    @property
    def status_code(self) -> int:
        return self.__status_code.value

    @property
    def body(self) -> str:
        return self.__body
