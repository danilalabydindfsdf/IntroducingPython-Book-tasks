# create an inheritance
class Car():
    def exclaim(self):
        print('I am a car')


class Yugo(Car):
    # redefinition methods
    def exclaim(self):
        print('I am a Yugo')

    def need_a_push(self):
        print('A little help here?')


class Person():
    def __init__(self, name):
        self.name = name


class Doctor(Person):
    # when you define __init__() method for your own class, you replace the __init__() method of parent class, that
    # doesn't call auto now, and you need to do it clearly
    # 1: a super method gets the parent class definition
    # 2: the __init__() method calls the Person.__init__() method. it passes a self argument to the parent class
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Doctor ' + name


def main():
    # check does that class inheritance by the other class
    print(issubclass(Yugo, Car))  # true

    # create objects for every claas
    # the yugo class inherited the exclaim method of the Car class
    car = Car()
    yugo = Yugo()
    car.exclaim()
    yugo.exclaim()
    yugo.need_a_push()

    # in this case, the __init__() method takes the same arguments as a parent class, but stores it in different ways
    person = Person('Fudd')
    doctor = Doctor('Fudd')
    print(person.name)
    print(doctor.name)

    print(Car.mro())

    a = set(range(10))
    print(a)
    a.add(10)
    print(a)


if __name__ == '__main__':
    main()
