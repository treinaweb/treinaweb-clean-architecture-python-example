from typing import List

from clean_arch_python.enterprise.entities.client import Client
from clean_arch_python.application.gateways.client_gateways import ClientGateway
from clean_arch_python.infra.db.mysql_db import connect


class ClientInMemoryGateway(ClientGateway):
    __clients: List[Client] = [
        Client("test", "test", "test@mail.com", "12345678912"),
    ]

    def find_all(self) -> List[Client]:
        return ClientInMemoryGateway.__clients.copy()

    def create(self, client: Client) -> None:
        ClientInMemoryGateway.__clients.append(client)


class ClientMySQLGateway(ClientGateway):
    def find_all(self) -> List[Client]:
        with connect() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM clients")
            result = cursor.fetchall()
            return [
                Client(
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                )
                for row in result
            ]

    def create(self, client: Client) -> None:
        with connect() as connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO clients (nome, sobrenome, email, cpf) VALUES (%s, %s, %s, %s)",
                (client.first_name, client.last_name, client.email, client.cpf),
            )
            connection.commit()
