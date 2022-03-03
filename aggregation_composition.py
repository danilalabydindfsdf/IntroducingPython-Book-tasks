class Bill():
    def __init__(self, description):
        self.description = description


class Tail():
    def __init__(self, length):
        self.length = length


class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print(f'The duck has a {self.bill.description} bill and a {self.tail.length} tail')


def main():
    a_tail = Tail('long')
    a_bill = Bill('wide orange')
    print(a_tail.length)
    print(a_bill.description)
    duck = Duck(a_bill, a_tail)
    duck.about()
    

if __name__ == '__main__':
    main()
