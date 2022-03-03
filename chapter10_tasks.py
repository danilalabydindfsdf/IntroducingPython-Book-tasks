class Thing():
    ...


class Thing2():
    letters = 'abc'


class Thing3():
    def __init__(self):
        self.letters = 'xyz'


class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        return self.name, self.symbol, self.number


class HiddenElement():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

class Bear():
    @staticmethod
    def eats():
        return 'berries'


class Rabbit():
    @staticmethod
    def eats():
        return 'clover'


class Octothorpe():
    @staticmethod
    def eats():
        return 'campers'


class Laser():
    @staticmethod
    def does():
        return 'disintegrate'


class Claw():
    @staticmethod
    def does():
        return 'crush'


class SmartPhone():
    @staticmethod
    def does():
        return 'ring'


class Robot():
    def __init__(self, laser, claw, smartphone):
        self.laser = laser
        self.claw = claw
        self.smartphone = smartphone

    def does(self):
        return self.laser.does(), self.claw.does(), self.smartphone.does()


def main():
    # 10.1
    print(Thing)
    example = Thing()
    print(example)

    # 10.2
    print(Thing2.letters)

    # 10.3
    print(Thing3)
    test = Thing3()
    print(test.letters)

    # 10.4
    simple_element = Element('Hydrogen', 'H', 1)

    # 10.5
    a = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
    hydrogen = Element(name=a['name'], symbol=a['symbol'], number=a['number'])
    print(hydrogen.name)

    hydrogen2 = Element(**a)
    print(hydrogen2.name)

    # 10.6
    hydrogen3 = Element(**a)
    print(hydrogen3.dump())

    # 10.7
    print(hydrogen3)

    # 10.8
    #hydro = HiddenElement('Hydrogen', 'H', 3)
    #print(hydro.name)

    # 10.9
    bear = Bear()
    rabbit = Rabbit()
    octo = Octothorpe()
    print(bear.eats())
    print(rabbit.eats())
    print(octo.eats())

    # 10.10
    laser = Laser()
    claw = Claw()
    smartphone = SmartPhone()
    robot = Robot(laser, claw, smartphone)
    print(robot.laser.does())
    print(robot.claw.does())
    print(robot.smartphone.does())
    print(robot.does())


if __name__ == '__main__':
    main()
