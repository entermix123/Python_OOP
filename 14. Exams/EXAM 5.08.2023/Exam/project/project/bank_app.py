from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    ALLOWED_LOAN_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    ALLOWED_CLIENT_TYPES = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.ALLOWED_LOAN_TYPES:
            raise Exception("Invalid loan type!")

        self.loans.append(self.ALLOWED_LOAN_TYPES[loan_type]())
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):

        if client_type not in self.ALLOWED_CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        self.clients.append(self.ALLOWED_CLIENT_TYPES[client_type](client_name, client_id, income))
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan = [x for x in self.loans if x.__class__.__name__ == loan_type][0]
        client = [x for x in self.clients if x.client_id == client_id][0]

        if (client.__class__.__name__ == "Student" and loan.__class__.__name__ != "StudentLoan") or \
                (client.__class__.__name__ != "Student" and loan.__class__.__name__ == "StudentLoan"):
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        clients = [x for x in self.clients if x.client_id == client_id]

        if not clients:
            raise Exception("No such client!")
        client = clients[0]

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        count = 0
        loans = [x for x in self.loans if x.__class__.__name__ == loan_type]
        if loans:
            for loan in loans:
                loan.increase_interest_rate()
                count += 1

        return f"Successfully changed {count} loans."

    def increase_clients_interest(self, min_rate: float):
        clients = [x for x in self.clients if x.interest < min_rate]
        count = 0

        if clients:
            for client in clients:
                client.increase_clients_interest()
                count += 1

        return f"Number of clients affected: {count}."

    def get_statistics(self):
        total_client_income = 0
        count_granted_loans = 0
        granted_loans_total_sum = 0
        available_loans = len(self.loans)
        total_sum_available_loans = sum([x.amount for x in self.loans])

        clients_count = len(self.clients)
        if clients_count > 0:
            average_client_interest_rate = sum(x.interest for x in self.clients) / clients_count
        else:
            average_client_interest_rate = 0

        if self.clients:
            for client in self.clients:
                total_client_income += client.income

                if client.loans:
                    for loan in client.loans:
                        count_granted_loans += 1
                        loan_amount = loan.amount
                        granted_loans_total_sum += loan_amount

        result = f"Active Clients: {clients_count}\n"
        result += f"Total Income: {total_client_income:.2f}\n"
        result += f"Granted Loans: {count_granted_loans}, Total Sum: {granted_loans_total_sum:.2f}\n"
        result += f"Available Loans: {available_loans}, Total Sum: {total_sum_available_loans:.2f}\n"
        result += f"Average Client Interest Rate: {average_client_interest_rate:.2f}"
        return result
