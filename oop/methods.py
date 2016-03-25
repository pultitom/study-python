import abc
""" reference: https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods """

class BasePizza(object):
    __metaclass__ = abc.ABCMeta

    ingredients = ['cheese']

    @classmethod
    @abc.abstractmethod
    def get_ingredients(cls):
        """ Returns ingredient list """
        return cls.ingredients



class Pizza(BasePizza):
    radius = 42

    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size

    @staticmethod
    def mix_ingredients(x, y):
        return x + y

    @classmethod # Usages: factory methods, that are used to create an instance for a class using for example some sort of pre-processing. If we use a @staticmethod instead, we would have to hardcode the Pizza class name in our function, making any class inheriting from Pizza unable to use our factory for its own use.
    def get_radius(cls):
        return cls.radius

    def cook(self):
        return self.mix_ingredients(self.cheese, self.vegetables)


print(Pizza.get_size(Pizza(42)))
print(Pizza(30).get_size())

method = Pizza(15).get_size
print(method())

print(Pizza.get_radius())
