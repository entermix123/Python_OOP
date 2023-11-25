from typing import List

from project_gym.customer import Customer
from project_gym.equipment import Equipment
from project_gym.exercise_plan import ExercisePlan
from project_gym.subscription import Subscription
from project_gym.trainer import Trainer


class Gym:

    customers: List[Customer] = []
    trainers: List[Trainer] = []
    equipment: List[Equipment] = []
    plans: List[ExercisePlan] = []
    subscriptions: List[Subscription] = []

    @classmethod
    def add_customer(cls, customer: Customer):
        if customer not in cls.customers:
            cls.customers.append(customer)

    @classmethod
    def add_trainer(cls, trainer: Trainer):
        if trainer not in cls.trainers:
            cls.trainers.append(trainer)

    @classmethod
    def add_equipment(cls, equipment: Equipment):
        if equipment not in cls.equipment:
            cls.equipment.append(equipment)

    @classmethod
    def add_plan(cls, plan: ExercisePlan):
        if plan not in cls.plans:
            cls.plans.append(plan)

    @classmethod
    def add_subscription(cls, subscription: Subscription):
        if subscription not in cls.subscriptions:
            cls.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = [x for x in self.subscriptions if x.id == subscription_id][0]
        customer = [x for x in self.customers if x.id == subscription.customer_id][0]
        trainer = [x for x in self.trainers if x.id == subscription.trainer_id][0]
        plan = [x for x in self.plans if x.id == subscription.exercise_id][0]
        equipment = [x for x in self.equipment if x.id == subscription.exercise_id][0]
        result = [f"{subscription}", f"{customer}", f"{trainer}", f"{equipment}", f"{plan}"]
        return '\n'.join(result)
