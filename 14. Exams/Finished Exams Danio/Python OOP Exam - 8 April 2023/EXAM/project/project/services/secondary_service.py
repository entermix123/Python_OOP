# from project.robots.female_robot import FemaleRobot
# from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name, capacity=15):
        super().__init__(name, capacity)

    def details(self):
        if not self.robots:
            return f"{self.name} Secondary Service:\nRobots: none"

        robots = [x.name for x in self.robots]
        return f"{self.name} Secondary Service:\nRobots: {' '.join(robots)}"


# ser = SecondaryService('Test')
# fm_rob = FemaleRobot('Blonde', 'prostitute', 250.0)
# ml_rob = MaleRobot('Dick', 'Pimp', 400.0)
# ser.robots = [fm_rob, ml_rob]
# print(ser.details())
