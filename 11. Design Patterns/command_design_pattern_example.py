from abc import ABC, abstractmethod


class Command(ABC):     # base abstract class Command

    @abstractmethod     # abstract method children classes must implement
    def execute(self):
        pass


class LightOnCommand(Command):  # create class for specific command inheriting class Command, must have execute() method

    def __init__(self, light):      # initialize command object
        self.light = light

    def execute(self):              # implement execute command
        self.light.on()


class LightOffCommand(Command):  # create class for specific command inheriting class Command, must have execute() method

    def __init__(self, light):  # initialize command object
        self.light = light

    def execute(self):          # implement execute command
        self.light.off()


class Light:                        # create class Light

    def on(self):                   # method on()
        print("Light in on")

    def off(self):                  # method off()
        print("Light in ff")


class RemoteControl:            # create class RemoteControl

    def __init__(self):         # initialize instance
        self.commands = {}      # create dictionary for commands

    def add_command(self, name, command):       # add command to dictionary
        self.commands[name] = command

    def execute_command(self, name):       # execute command if in dictionary
        if name in self.commands:          # iterate true command dictionary
            self.commands[name].execute()  # find command and execute it: LightOnCommand(light) or LightOffCommand(light)
        else:
            print("Command not found")     # print text if command not found


light = Light()
light_on_command = LightOnCommand(light)                # create instance of LightOnCommand
light_off_command = LightOffCommand(light)              # create instance of LightOffCommand

remote_control = RemoteControl()                        # create instance of RemoteControl
remote_control.add_command("on", light_on_command)      # add command on to dictionary
remote_control.add_command("off", light_off_command)    # add command off to dictionary

remote_control.execute_command("on")                    # execute command on
remote_control.execute_command("off")                   # execute command off
remote_control.execute_command("none")                  # execute unknown command
