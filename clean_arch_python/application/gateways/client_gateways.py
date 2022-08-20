import abc
from typing import List

from clean_arch_python.enterprise.entities.client import Client


class ClientGateway(abc.ABC):
    @abc.abstractmethod
    def find_all(self) -> List[Client]:
        ...

    @abc.abstractmethod
    def create(self, client: Client) -> None:
        ...
