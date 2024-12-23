from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    ALLOWED_SERVICE_TYPES = {"MainService": MainService, "SecondaryService": SecondaryService}
    ALLOWED_ROBOT_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.ALLOWED_SERVICE_TYPES:
            raise Exception("Invalid service type!")

        self.services.append(self.ALLOWED_SERVICE_TYPES[service_type](name))
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.ALLOWED_ROBOT_TYPES:
            raise Exception("Invalid robot type!")

        self.robots.append(self.ALLOWED_ROBOT_TYPES[robot_type](name, kind, price))
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = [x for x in self.robots if x.name == robot_name][0]
        service = [x for x in self.services if x.name == service_name][0]

        if (robot.__class__.__name__ != "MaleRobot" and service.__class__.__name__ == "MainService") or \
                (robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ != "MainService"):
            return "Unsuitable service."

        if service.capacity <= len(self.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = [x for x in self.services if x.name == service_name][0]

        if robot_name not in [x.name for x in service.robots]:
            raise Exception("No such robot in this service!")

        robot = [x for x in service.robots if x.name == robot_name][0]
        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = [x for x in self.services if x.name == service_name][0]

        robots_fed = 0
        for rob in service.robots:
            rob.eating()
            robots_fed += 1

        return f"Robots fed: {robots_fed}."

    def service_price(self, service_name: str):
        service = [x for x in self.services if x.name == service_name][0]

        total_price = 0.0
        for rob in service.robots:
            total_price += rob.price

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = []
        for ser in self.services:
            result.append(ser.details())

        return '\n'.join(result)


# main_app = RobotsManagingApp()
# ser = SecondaryService('Test')
# fm_rob = FemaleRobot('Blonde', 'prostitute', 250.0)
# ml_rob = MaleRobot('Dick', 'Pimp', 400.0)
# main_app.robots = [fm_rob, ml_rob]
# main_app.services = [ser]
# print(RobotsManagingApp.add_robot_to_service(main_app, 'Blonde', 'Test'))

