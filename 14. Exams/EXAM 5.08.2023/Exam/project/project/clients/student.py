from project.clients.base_client import BaseClient


class Student(BaseClient):
    interest_hike = 1.0

    def __init__(self, name, client_id, income, interest=2.0):
        super().__init__(name, client_id, income, interest)

    def increase_clients_interest(self):
        self.interest += self.interest_hike
