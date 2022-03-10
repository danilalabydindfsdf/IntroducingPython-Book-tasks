# create a class that represents a real-world object (a cat for example)
class MyCat():
    ...


class Cat():
    # if you want to assign attributes to an object, you need to use a special method called '__init__'
    # it is a special method that initialize an object by definition of its class,
    # the 'self' argument maps to the object itself
    def __init__(self, name):
        self.name = name


def main():
    # to create an object of any Class, use the following construction
    my_cat = MyCat()
    another_cat = MyCat()
    print(my_cat)
    print(another_cat)

    # attribute is a variable that locates inside a class or object
    my_cat.age = 10
    my_cat.name = 'Philya'
    print(my_cat.age, my_cat.name)

    # attribute can reference to other object
    my_cat.nemesis = another_cat
    print(my_cat.nemesis)

    # if you want to get access to different objects attributes, make sure the object has any attributes
    try:
        print(my_cat.nemesis.name)
    except AttributeError as err:
        print(err)
    my_cat.nemesis.name = 'Marysya'
    print(my_cat.nemesis.name)

    # now you can create an object by passing a string for name parameter
    # the next string will make this:
    # 1: searches the definition of the 'Cat' class
    # 2: creates a new object in memory
    # 3: calls the __init__() method, passes a new object(with 'self' name), and argument 'blacky' as a name parameter
    # 4: stores the value of a name variable in the object
    # 5: returns the new object
    # 6: binds the new object with 'black_cat' variables
    black_cat = Cat('blacky')

    print(black_cat)
    print(black_cat.name)


if __name__ == '__main__':
    main()
