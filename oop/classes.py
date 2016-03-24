# Guido van Rossum has designed the language according to the principle "first-class everything"

x = 42
print(type(x)) # prints: <class 'int'>

class Robot:

    __number_of_instances = 0

      # name   Public These attributes can be freely used inside or outside of a class definition.
      # _name   Protected Protected attributes should not be used outside of the class definition, unless inside of a subclass definition.
      # __name  Private This kind of attribute is inaccessible and invisible. It's neither possible to read nor write to those attributes, except inside of the class definition itself.
    def __init__(self, name, build_year):
        self.__name = name # private property
        self.build_year = build_year
        Robot.increase_counter()
        print("__init__ has been executed!")

# he first parameter in the definition of a method has to be a reference to the instance, which called the method. This parameter is usually called "self".
    def say_hello(self):
        print("Hello " + self.__name)

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @staticmethod
    def increase_counter():
        Robot.__number_of_instances += 1

    @staticmethod
    def decrease_counter():
        Robot.__number_of_instances -= 1

    @staticmethod
    def get_number_of_instances():
        return Robot.__number_of_instances

    def __str__(self):
        return "Robot " + self.__name + " made in " + str(self.build_year)

    def __repr__(self):
        return "Robot " + self.__name + " made in " + str(self.build_year)

    def __del__(self):
        print(self.__name + " says bye bye")
        type(self).decrease_counter()


Robot.name = "robot"
robot = Robot("Megatron", 2136)
robot.color = "red"
print("number of robots: " + str(Robot.get_number_of_instances()))

Robot.increase_counter()
print("increased number of robots")
print("number of robots: " + str(Robot.get_number_of_instances()))

robot.say_hello()
print(robot.__dict__) # prints all class properties and their values
print(Robot.__dict__) # prints all class properties and their values
print(robot)
print("robot.get_name() == " + robot.get_name())
new_robot_name = "Optimus prime"
print("new_robot_name = " + new_robot_name)
robot.set_name(new_robot_name)

new_robot = Robot("Megatron", 2137)
print("number of robots: " + str(Robot.get_number_of_instances()))

print("robot.get_name() == " + robot.get_name())
del new_robot

try:
    x = robot.non_exiting_param
except AttributeError:
    print("Throws error when we call non-existing parameter")

x = getattr(robot, 'non_existing_param', 100) #sets default value if attribute doesn't exist
print(x)

try:
    y = robot.__name
except AttributeError:
    print("Can't reach private attribute")


print("number of robots: " + str(Robot.get_number_of_instances()))
