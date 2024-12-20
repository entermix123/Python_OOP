from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    interest_rate_hike = 0.5

    def __init__(self, interest_rate=3.5, amount=50000.0):
        super().__init__(interest_rate, amount)

    def increase_interest_rate(self):
        self.interest_rate += self.interest_rate_hike
