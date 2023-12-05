from abc import abstractmethod, ABC


class Duck(ABC):

    def __init__(self):     # made the __init__ in base class
        self.height = 0

    @abstractmethod     # changed from staticmethod to abstractmethod
    def quack(self):
        pass

    @abstractmethod     # changed from staticmethod to abstractmethod
    def walk(self):
        pass

    @abstractmethod     # changed from staticmethod to abstractmethod, moved from RobotDuck class
    def fly(self):
        pass

    @classmethod        # moved from RobotDuck class and changed to class method
    def land(cls):
        cls.height = 0


class RubberDuck(Duck):

    def quack(self):        # changed from staticmethod to abstractmethod
        return "Squeek"

    def walk(self):         # changed from staticmethod to abstractmethod
        """Rubber duck can walk only if you move it"""
        raise NotImplementedError('I cannot walk by myself')    # notimplemented method message

    def fly(self):          # changed from staticmethod to abstractmethod
        """Rubber duck can fly only if you throw it"""
        raise NotImplementedError('I cannot fly by myself')     # notimplemented method message


class RobotDuck(Duck):
    HEIGHT = 50

    def quack(self):            # changed from staticmethod to abstractmethod
        return 'Robotic quacking'

    def walk(self):             # changed from staticmethod to abstractmethod
        return 'Robotic walking'

    def fly(self):              # changed from staticmethod to abstractmethod
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1
