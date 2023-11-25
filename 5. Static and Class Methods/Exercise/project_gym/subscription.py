class Subscription:
    id = 1      # start id of the subscription

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = Subscription.get_next_id()    # automatic get id from get_next_id() static method
        Subscription.id += 1                    # auto increase the id

    @staticmethod
    def get_next_id():
        return Subscription.id

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"
