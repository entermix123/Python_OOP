from typing import List

from project_zoo.animal import Animal
from project_zoo.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):  # initialize for main class
        self.name = name                            # public attribute
        self.__budget = budget                      # private attribute
        self.__animal_capacity = animal_capacity    # private attribute
        self.__workers_capacity = worker_capacity   # private attribute
        self.animals: List[Animal] = []             # list of instances from class Animal
        self.workers: List[Worker] = []             # list of instances from class Worker

    def add_animal(self, animal: Animal, price: int):   # create add animal class method

        # check if price is enough to add animal and if enough capacity
        if self.__budget > price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        # if budget is not enough to add animal
        elif self.__budget < price:
            return f"Not enough budget"

        # in every other case
        else:
            return f"Not enough space for animal"

    def hire_worker(self, worker: Worker):              # create hire worker class method
        if self.__workers_capacity > len(self.workers):  # check if there is enough space to hire worker
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        # if not enough space to hire worker
        else:
            return f"Not enough space for worker"

    def fire_worker(self, worker_name: str):    # create fire worker class method
        try:                                    # create try error case
            # find worker by name in collection of workers
            worker = next(filter(lambda x: x.name == worker_name, self.workers))
        # if worker is not found
        except StopIteration:
            return f"There is no {worker_name} in the zoo"  # raise error

        # if worker is found of workers
        self.workers.remove(worker)                 # remove worker from collection of workers
        return f"{worker.name} fired successfully"  # print message

    def pay_workers(self):
        # sum_pay_workers = sum(k.salary for k in self.workers)
        sum_pay_workers = 0
        for worker in self.workers:
            sum_pay_workers += worker.salary
        if sum_pay_workers <= self.__budget:
            self.__budget -= sum_pay_workers
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        # sum_care_animals = sum(animal.money_for_care for animal in self.animals)
        sum_care_animals = 0
        for animal in self.animals:
            sum_care_animals += animal.money_for_care
        if sum_care_animals <= self.__budget:
            self.__budget -= sum_care_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        # lions = list(filter(lambda x: x.__class__.__name__ == "Lion", self.animals))
        # tigers = list(filter(lambda x: x.__class__.__name__ == "Tiger", self.animals))
        # cheetahs = list(filter(lambda x: x.__class__.__name__ == "Cheetah", self.animals))
        #
        # result = [
        #     f"You have {len(self.animals)} animals",
        #     f"----- {len(lions)} Lions:"
        # ]
        # result.extend(lions)
        #
        # result.append(f"----- {len(tigers)} Tigers:")
        # result.extend(tigers)
        #
        # result.append(f"----- {len(cheetahs)} Cheetahs:")
        # result.extend(cheetahs)
        #
        # return '\n'.join(str(x) for x in result)

        lions = [x for x in self.animals if x.__class__.__name__ == "Lion"]
        lions_str = [f"----- {len(lions)} Lions:"]
        [lions_str.append(f"{lion.__repr__()}") for lion in lions]

        cheetahs = [y for y in self.animals if y.__class__.__name__ == "Cheetah"]
        cheetahs_str = [f"----- {len(cheetahs)} Cheetahs:"]
        [cheetahs_str.append(f"{cheetah.__repr__()}") for cheetah in cheetahs]

        tigers = [z for z in self.animals if z.__class__.__name__ == "Tiger"]
        tigers_str = [f"----- {len(tigers)} Tigers:"]
        [tigers_str.append(f"{tiger.__repr__()}") for tiger in tigers]

        return f"You have {len(self.animals)} animals\n" + "\n".join(lions_str) \
            + "\n" + "\n".join(tigers_str) + "\n" + "\n".join(cheetahs_str)

    def workers_status(self):
        # info = {"Keeper": [], "Caretaker": [], "Vet": []}
        # [info[p.__class__.__name__].append(str(p)) for p in self.workers]
        #
        # result = [
        #     f"You have {len(self.workers)} workers",
        #     f"----- {len(info['Keeper'])} Keepers:",
        #     *info['Keeper'],
        #     f"----- {len(info['Caretaker'])} Caretakers:",
        #     *info['Caretaker'],
        #     f"----- {len(info['Vet'])} Vets:",
        #     *info['Vet']
        # ]
        #
        # return '\n'.join(result)

        keepers = [x for x in self.workers if x.__class__.__name__ == "Keeper"]
        keepers_str = [f"----- {len(keepers)} Keepers:"]
        [keepers_str.append(f"{keeper.__repr__()}") for keeper in keepers]

        caretakers = [y for y in self.workers if y.__class__.__name__ == "Caretaker"]
        caretakers_str = [f"----- {len(caretakers)} Caretakers:"]
        [caretakers_str.append(f"{caretaker.__repr__()}") for caretaker in caretakers]

        vets = [z for z in self.workers if z.__class__.__name__ == "Vet"]
        vets_str = [f"----- {len(vets)} Vets:"]
        [vets_str.append(f"{vet.__repr__()}") for vet in vets]

        return f"You have {len(self.workers)} workers\n" + '\n'.join(keepers_str) + \
            '\n' + '\n'.join(caretakers_str) + '\n' + '\n'.join(vets_str)
