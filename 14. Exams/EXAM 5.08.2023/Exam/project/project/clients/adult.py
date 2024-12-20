from project.clients.base_client import BaseClient


class Adult(BaseClient):
    interest_hike = 2.0

    def __init__(self, name, client_id, income, interest=4.0):
        super().__init__(name, client_id, income, interest)

    def increase_clients_interest(self):
        self.interest += self.interest_hike
