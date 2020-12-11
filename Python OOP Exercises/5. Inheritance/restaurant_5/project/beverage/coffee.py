from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):

    COFFEE_PRICE = 3.50
    COFFEE_MILLILITERS = 50

    def __init__(self, name, caffeine):
        super().__init__(name, self.__class__.COFFEE_MILLILITERS, self.__class__.COFFEE_PRICE)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

    @caffeine.setter
    def caffeine(self, val):
        self.__caffeine = val