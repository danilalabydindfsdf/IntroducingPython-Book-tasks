from dataclasses import dataclass


@dataclass
class AnimalClass:
    name: str
    habitat: str
    teeth: int = 0


def main():
    snowman = AnimalClass('yeti', 'Himalayas', 46)
    duck = AnimalClass(habitat='lake', name='duck')
    print(snowman)
    print(duck)
    print(duck.teeth)
    

if __name__ == '__main__':
    main()
