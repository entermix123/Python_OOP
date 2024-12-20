from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    interest_rate_hike = 0.2

    def __init__(self, interest_rate=1.5, amount=2000.0):
        super().__init__(interest_rate, amount)

    def increase_interest_rate(self):
        self.interest_rate += self.interest_rate_hike
