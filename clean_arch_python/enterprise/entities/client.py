from clean_arch_python.enterprise.entities.email import Email
from clean_arch_python.enterprise.entities.cpf import Cpf


class ClientName:
    def __init__(self, value: str) -> None:
        if len(value) < 3:
            raise ValueError("Client name must have at least 3 letters")
        if not value.isalpha():
            raise ValueError("Client name must have letters only")
        self.__value = value

    @property
    def value(self) -> str:
        return self.__value


class Client:
    def __init__(self, first_name: str, last_name: str, email: str, cpf: str) -> None:
        self.__first_name = ClientName(first_name)
        self.__last_name = ClientName(last_name)
        self.__email = Email(email)
        self.__cpf = Cpf(cpf)

    @property
    def first_name(self) -> str:
        return self.__first_name.value

    @property
    def last_name(self) -> str:
        return self.__last_name.value

    @property
    def email(self) -> str:
        return self.__email.value

    @property
    def cpf(self) -> str:
        return self.__cpf.value
