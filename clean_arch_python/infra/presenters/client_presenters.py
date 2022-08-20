import json
from typing import List

from clean_arch_python.enterprise.entities.client import Client


class FindAllClientsOutputBoundary:
    @staticmethod
    def to_json(clients: List[Client]) -> str:
        if clients is None:
            return "[]"
        return json.dumps(
            [
                {
                    "first_name": client.first_name,
                    "last_name": client.last_name,
                    "email": client.email,
                    "cpf": client.cpf,
                }
                for client in clients
            ]
        )


class CreateClientInputBoundary:
    @staticmethod
    def from_json(json_data: str) -> Client:
        data = json.loads(json_data)
        return Client(
            data["first_name"],
            data["last_name"],
            data["email"],
            data["cpf"],
        )


class CreateClientOutputBoundary:
    @staticmethod
    def to_json(client: Client) -> str:
        if client is None:
            return "{}"
        return json.dumps(
            {
                "first_name": client.first_name,
                "last_name": client.last_name,
                "email": client.email,
                "cpf": client.cpf,
            }
        )
