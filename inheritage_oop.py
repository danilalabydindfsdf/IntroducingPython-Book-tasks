class Animal:
    def says(self):
        return 'I speak!'


class Horse(Animal):
    def says(self):
        return 'Neigh!'


class Donkey(Animal):
    def says(self):
        return 'Hee-haw'


class Mule(Donkey, Horse):
    pass


class Hinny(Horse, Donkey):
    pass


class PrettyMixin():
    def dump(self):
        import pprint
        pprint.pprint(vars(self))


class Thing(PrettyMixin):
    pass


print(Mule.mro())
mule = Mule()
hinny = Hinny()
print(mule.says())
print(hinny.says())
t = Thing()
t.name = 'aaa'
t.age = 133
t.dump()
