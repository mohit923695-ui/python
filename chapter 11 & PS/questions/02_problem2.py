#create a class 'pets' from a classs 'animals'and create a class 'dogs' from 'pets' add method 'bark' to class 'dog'


class animals():
    pass

class pets(animals):
    pass

class dogs(pets):
    @staticmethod
    def bark():
        print("Bow Bow")


d = dogs()
d.bark()
